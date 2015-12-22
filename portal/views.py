from django.shortcuts import render
from django.shortcuts import render_to_response,redirect
from django.http import HttpResponseRedirect, HttpResponse
from django.template import RequestContext
from .forms import *
from django.contrib.auth.models import User
from .models import *
from django.contrib.auth import authenticate, login, logout
import json

# Create your views here.

def PuserRegistration(request):
	if request.user.is_authenticated():
		return HttpResponseRedirect('/posts/')
	if request.method == 'POST':
		form = RegistrationForm(request.POST)
		if form.is_valid():
			user = User.objects.create_user(username = form.cleaned_data['username'],password = form.cleaned_data['password'])
			user.save()
			stu = Puser( user =user,
						 orgname = form.cleaned_data['orgname'],
						 email = form.cleaned_data['email'],
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
		return HttpResponseRedirect('/posts/')
	if request.method == "POST":
		form = LoginForm(request.POST)
		if form.is_valid():

			username = form.cleaned_data['username']
			password = form.cleaned_data['password']
			student = authenticate(username=username, password=password)
			if student is not None:
				login(request, student)
				return HttpResponseRedirect('/posts/')
			else:
				return HttpResponseRedirect('/login/')
				#return render_to_response('login.html',context,context_instance = RequestContext(request))
		else:
			return render_to_response('login.html',context,context_instance = RequestContext(request))




	else:
		form = LoginForm()
		context = {'form': form}
		return render_to_response('login.html',context,context_instance = RequestContext(request))

def LogoutRequest(request):
	logout(request)
	return HttpResponseRedirect('/')

def StartPage(request):
	if request.user.is_authenticated():
		return HttpResponseRedirect('/posts/')
	else:
		return HttpResponseRedirect('/login/')


def PostsView(request):
	u = request.user
	pu = Puser.objects.get(user = u)
	comments = Comment.objects.all()
	if request.method == "POST":
		form = PostForm(request.POST)
		if form.is_valid():
			body = form.cleaned_data['body']
			newpost = Post(user = pu,body = body)
			newpost.save()
			return HttpResponseRedirect('http://127.0.0.1:8000/posts/')
		else:
			postform = PostForm()
			posts = Post.objects.all()
			context = { 'postform':postform,
					'posts': posts,
					'comments': comments,
				   	}
			return render_to_response('posts.html',context,context_instance  = RequestContext(request))

	else:
		postform = PostForm()
		posts = Post.objects.all()
		context = { 'postform':postform,
					'posts': posts,
					'comments':comments,
				   	}
		return render_to_response('posts.html',context,context_instance  = RequestContext(request))


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

def QueriesView(request):
	u = request.user
	pu = Puser.objects.get(user = u)

	if request.method == "POST":
		form = QueryForm(request.POST)
		if form.is_valid():
			body = form.cleaned_data['body']
			newquery = Query(user = pu,body = body)
			newquery.save()
			return HttpResponseRedirect('http://127.0.0.1:8000/queries/')
		else:
			queryform = QueryForm()
			queries = Query.objects.all()
			context = { 'queryform':queryform,
					'queries': queries,
				   	}
			return render_to_response('queries.html',context,context_instance  = RequestContext(request))

	else:
		queryform = QueryForm()
		queries = Query.objects.all()
		context = { 'queryform':queryform,
					'queries': queries,
				   	}
		return render_to_response('queries.html',context,context_instance  = RequestContext(request))
