from django.shortcuts import render
from django.shortcuts import render_to_response,redirect
from django.http import HttpResponseRedirect, HttpResponse
from django.template import RequestContext
from .forms import *
from django.contrib.auth.models import User
from .models import *
from django.contrib.auth import authenticate, login, logout

# Create your views here.

def PuserRegistration(request):
	if request.user.is_authenticated():
		return HttpResponseRedirect('/forum/')
	if request.method == 'POST':
		form = RegistrationForm(request.POST)
		if form.is_valid():
			user = User.objects.create_user(username = form.cleaned_data['username'],password = form.cleaned_data['password'])
			user.save()
			
			stu = Puser(user =user, name = form.cleaned_data['name'],	email = form.cleaned_data['email'])
			stu.save()
			stu.course = form.cleaned_data['courses']
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
		return HttpResponseRedirect('/forum/')
	if request.method == "POST":
		form = LoginForm(request.POST)
		if form.is_valid():

			username = form.cleaned_data['username']
			password = form.cleaned_data['password']
			student = authenticate(username=username, password=password)
			if student is not None:
				login(request, student)
				return HttpResponseRedirect('/forum/')
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
		return HttpResponseRedirect('/forum/')
	else:
		return HttpResponseRedirect('/login/')