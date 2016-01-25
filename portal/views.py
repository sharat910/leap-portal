from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.shortcuts import render_to_response,redirect
from django.http import HttpResponseRedirect, HttpResponse
from django.template import RequestContext
from .forms import *
from django.contrib.auth.models import User
from .models import *
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
import json
from django.db.models import Q

# Create your views here.

def PuserRegistration(request):
	if request.user.is_authenticated():
		return HttpResponseRedirect('/home/')
	if request.method == 'POST':
		form = RegistrationForm(request.POST,request.FILES)
		if form.is_valid():
			user = User.objects.create_user(username = form.cleaned_data['username'],password = form.cleaned_data['password'])
			user.save()
			stu = Puser( user =user,
						 orgname = form.cleaned_data['orgname'],
						 email = form.cleaned_data['email'],
						 image = request.FILES.get('image', False),
						 designation = form.cleaned_data['designation'],
						 location=form.cleaned_data['location'],
						 institution = form.cleaned_data['institution'],
						)
			stu.save()
			return HttpResponseRedirect('/login/')
		else:
			return render_to_response('register.html', {'form': form}, context_instance = RequestContext(request))
	else:
		''' user hasnt submitted the form, pop up the blank form'''
		form = RegistrationForm()
		context = {'form' : form}
		return render_to_response('register.html',context,context_instance = RequestContext(request))

def LoginRequest(request):
	if request.user.is_authenticated():
		return HttpResponseRedirect('/home/')
	else:
		form = LoginForm(request.POST or None)
		if form.is_valid():
			username = form.cleaned_data['username']
			password = form.cleaned_data['password']
			student = authenticate(username=username, password=password)
			if student is not None:
				login(request, student)
				return HttpResponseRedirect('/home/')
			else:
				return HttpResponseRedirect('/login/')
		context = {'form': form}
		return render_to_response('login1.html',context,context_instance = RequestContext(request))

@login_required
def LogoutRequest(request):
	logout(request)
	return HttpResponseRedirect('/')

def StartPage(request):
	if request.user.is_authenticated():
		return HttpResponseRedirect('/home/')
	else:
		return HttpResponseRedirect('/login/')

@login_required
def PostsView(request):
	u = request.user
	pu = Puser.objects.get(user = u)
	comments = Comment.objects.all()
	form = PostForm(request.POST or None)
	posts = Post.objects.all()
	context = { 'postform':form,
				'posts': posts,
				'comments':comments,
				'pu':pu,
			   	}
	if form.is_valid():
		body = form.cleaned_data['body']
		newpost = Post(user = pu,body = body)
		newpost.save()
		form = PostForm()
		context = { 'postform':form,
					'posts': posts,
					'comments':comments,
					'pu':pu,
				   	}

	return render_to_response('home.html',context,context_instance  = RequestContext(request))

@login_required
def CommentView(request):
	u = request.user
	pu = Puser.objects.get(user = u)
	postid = request.POST.get("post_id")
	body  = request.POST.get("body")
	post = Post.objects.get(pk = postid)
	comment = Comment(body = body,post = post,user = pu)
	comment.save()
	response_data = {}
	try:
		response_data['message'] = str(body)
	except:
		response_data['message'] = "Oops!"
	return HttpResponse(json.dumps(response_data), content_type = "application/json")

@login_required
def AnswerView(request):
	u = request.user
	pu = Puser.objects.get(user = u)
	queryid = request.POST.get("query_id")
	body  = request.POST.get("body")
	if not body == "":
		query = Query.objects.get(pk = queryid)
		answer = Answer(body = body,query = query,user = pu)
		answer.save()
	response_data = {}
	try:
		response_data['message'] = str(body)
	except:
		response_data['message'] = "Oops!"
	return HttpResponse(json.dumps(response_data), content_type = "application/json")

@login_required
def QueriesView(request):
	u = request.user
	pu = Puser.objects.get(user = u)
	answers = Answer.objects.all()
	form = QueryForm(request.POST or None)
	queries = Query.objects.all()
	context = { 'queryform':form,
				'queries': queries,
				'answers':answers,
				'pu':pu,
				}
	if form.is_valid():
		body = form.cleaned_data['body']
		newquery = Query(user = pu,body = body)
		newquery.save()
		form = QueryForm()
		context = { 'queryform':form,
					'queries': queries,
					'answers':answers,
					'pu':pu,
					}
	return render_to_response('home1.html',context,context_instance  = RequestContext(request))

@login_required
def MyQueriesView(request):
	u = request.user
	pu = Puser.objects.get(user = u)
	answers = Answer.objects.all()
	form = QueryForm(request.POST or None)
	queries = Query.objects.filter(user = pu)
	context = { 'queryform':form,
				'queries': queries,
				'answers':answers,
				'pu':pu,
				}
	if form.is_valid():
		body = form.cleaned_data['body']
		newquery = Query(user = pu,body = body)
		newquery.save()
		form = QueryForm()
		context = { 'queryform':form,
					'queries': queries,
					'answers':answers,
					'pu':pu,
					}
	return render_to_response('myqueries.html',context,context_instance  = RequestContext(request))

@login_required
def SearchQueriesView(request):
	u = request.user
	pu = Puser.objects.get(user = u)
	form = SearchForm(request.POST or None)
	context = { 'searchform':form,
				'pu':pu,
				}
	if form.is_valid():
		body = form.cleaned_data['body']
		results = Query.objects.filter(Q(body__icontains = body))
		form = SearchForm()
		context = { 'searchform':form,
					'results': results,
					'pu':pu,
					}
	return render_to_response('search.html',context,context_instance  = RequestContext(request))


@login_required
def EventView(request):
	u = request.user
	pu = Puser.objects.get(user = u)
	form = EventForm(request.POST or None, request.FILES or None)
	value = "Add Event"
	context = {	'form' : form,
			'pu' : pu,
			'value':value}
	if form.is_valid():
		event = Event(user = pu,
		name = form.cleaned_data['name'],
		description = form.cleaned_data['description'],
		details = request.FILES.get('details', False))
		event.save()
		body = "event"
		form = EventForm()
		context = {'body':body,
					'pu' : pu}
		return HttpResponseRedirect('/profile/' + u.username )

	return render_to_response('addevent.html',context,context_instance  = RequestContext(request))


@login_required
def AlumniView(request):
	u = request.user
	pu = Puser.objects.get(user = u)
	form = AlumniForm(request.POST or None)
	value = "Add Alumnus"
	context = {	'form' : form,
			'pu' : pu,
			'value':value}
	if form.is_valid():
		alumnus = Alumni(user = pu,
		name = form.cleaned_data['name'],
		about = form.cleaned_data['about'])
		alumnus.save()
		body = "alumnus"
		form = AlumniForm()
		context = {'body':body,
					'pu' : pu}
		return HttpResponseRedirect('/profile/' + u.username )

	return render_to_response('addalumni.html',context,context_instance  = RequestContext(request))

@login_required
def MediaView(request):
	u = request.user
	pu = Puser.objects.get(user = u)
	form = MediaForm(request.POST or None)
	value = "Add Media Publication"
	context = {	'form' : form,
			'pu' : pu,
			'value':value}
	if form.is_valid():
		media = Media(user = pu,
		title = form.cleaned_data['title'],
		description = form.cleaned_data['description'],
		link = form.cleaned_data['link'])
		media.save()
		body = "media publication"
		form = MediaForm()
		context = {'body':body,
					'pu' : pu}
		return HttpResponseRedirect('/profile/' + u.username )

	return render_to_response('addmedia.html',context,context_instance  = RequestContext(request))

@login_required
def ProjectView(request):
		u = request.user
		pu = Puser.objects.get(user = u)
		form = ProjectForm(request.POST or None, request.FILES or None)
		value = "Update Project"
		context = {	'form' : form,
				'pu' : pu,
				'value':value
				}
		if form.is_valid():
			proj = Project(user = pu,
			name = form.cleaned_data['name'],
			description = form.cleaned_data['description'],
			details = request.FILES.get('details', False),
			teamstrength = form.cleaned_data['teamstrength'],
			achievements = form.cleaned_data['achievements'],
			workingarea = form.cleaned_data['workingarea'])
			proj.save()
			body = "project"
			context = {'body':body,
						'pu' : pu}
			return HttpResponseRedirect('/profile/' + u.username )

		return render_to_response('addproject.html',context,context_instance  = RequestContext(request))

@login_required
def ProfileView(request,username):
	u = User.objects.get(username = username)
	pu = Puser.objects.get(user = u)
	projects = Project.objects.filter(user = pu)
	events = Event.objects.filter(user = pu)
	alumni = Alumni.objects.filter(user = pu)
	media  = Media.objects.filter(user = pu)
	context = {'pu':pu,
	'events':events,
	'projects':projects,
	'alumni':alumni,
	'media':media,
	}
	return render_to_response('profile1.html',context,context_instance  = RequestContext(request))

@login_required
def MentorView(request):
	u = request.user
	pu = Puser.objects.get(user = u)
	context = {'pu':pu,}
	return render_to_response('mentor.html',context,context_instance  = RequestContext(request))

##EDIT VIEWS

def EditPostView(request,id):
	post = get_object_or_404(Post,pk = id)
	if request.user == post.user.user:
		form = PostForm(request.POST or None,instance = post)
		if form.is_valid():
			form.save()
			print "edit post saved"
			return HttpResponseRedirect('/home/')

		context = {
		'post':post,
		'form':form
		}
		return render_to_response('editpost.html',context,context_instance  = RequestContext(request))
	else:
		return render_to_response('sorry.html')

def EditQueryView(request,id):
	query = get_object_or_404(Query,pk = id)
	if request.user == query.user.user:
		form = QueryForm(request.POST or None,instance = query)
		if form.is_valid():
			form.save()
			print "edit query saved"
			return HttpResponseRedirect('/queries/')

		context = {
		'query':query,
		'form':form
		}
		return render_to_response('editquery.html',context,context_instance  = RequestContext(request))
	else:
		return render_to_response('sorry.html')

def EditProfileView(request,username):
	u = User.objects.get(username = username)
	pu = Puser.objects.get(user = u)
	if request.user == pu.user:
		form = PuserForm(request.POST or None,request.FILES or None,instance = pu)
		if form.is_valid():
			form.save()
			print "edit query saved"
			return HttpResponseRedirect('/profile/' +  u.username)

		context = {
		'pu':pu,
		'form':form
		}
		return render_to_response('editprofile.html',context,context_instance  = RequestContext(request))
	else:
		return render_to_response('sorry.html')

def EditEventView(request,id):
	event = get_object_or_404(Event,pk = id)
	if request.user == event.user.user:
		form = EventForm(request.POST or None,instance = event)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect('/profile/' + str(request.user.username))
		value = "Update Event"
		context = {
		'event':event,
		'form':form,
		'value':value
		}
		return render_to_response('editevent.html',context,context_instance  = RequestContext(request))
	else:
		return render_to_response('sorry.html')

def EditProjectView(request,id):
	project = get_object_or_404(Project,pk = id)
	if request.user == project.user.user:
		form = EventForm(request.POST or None,instance = project)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect('/profile/' + str(request.user.username))
		value = "Update Project"
		context = {
		'project':project,
		'form':form,
		'value':value
		}
		return render_to_response('editproject.html',context,context_instance  = RequestContext(request))
	else:
		return render_to_response('sorry.html')

def CommunityView(request):
	pu = Puser.objects.all()
	context ={'pu': pu}
	return render_to_response('community.html',context,context_instance  = RequestContext(request))
