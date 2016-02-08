from django import forms
from django.contrib.auth.models import User
from django.forms import ModelForm
from .models import *
from material import *

class RegistrationForm(ModelForm):
	username = forms.CharField(label = (u'Username'))
	password = forms.CharField(label = (u'Password'), widget = forms.PasswordInput(render_value = False))

	class Meta:
		model = Puser
		exclude = ('user','joineddate','designation')

	def clean_username(self):
		username = self.cleaned_data['username']
		try:
			User.objects.get(username = username)
		except User.DoesNotExist:
			return username

		raise forms.ValidationError("That username is already taken.")


	def clean_password(self):
		password = self.cleaned_data['password']
		return password

class PuserForm(ModelForm):
	class Meta:
		model = Puser
		exclude = ('user','joineddate','designation',)


class LoginForm(forms.Form):
	username = forms.CharField(label = (u'UserName'),required = True)
	password = forms.CharField(label = (u'Password'), widget = forms.PasswordInput(render_value = False),required = True)

	layout = Layout('username','password')

class PassForm(forms.Form):
	username = forms.CharField(label = (u'UserName'),required = True)
	password = forms.CharField(label = (u'NewPassword'), widget = forms.PasswordInput(render_value = False),required = True)

	layout = Layout('username','password')

class PostForm(forms.ModelForm):
	body = forms.CharField(label=(u'Post'), required = True,widget=forms.Textarea)

	class Meta:
		model = Post
		fields = ['body']

	def clean_body(self):
		body = self.cleaned_data.get('body')
		return body


class QueryForm(forms.ModelForm):
	body = forms.CharField(label=(u'Query'), required = True,widget=forms.Textarea)


	class Meta:
		model = Query
		fields = ['body']

	def clean_body(self):
		body = self.cleaned_data.get('body')
		return body

class SearchForm(forms.Form):
	body = forms.CharField(label=(u'Search'), required = True)

	def clean_body(self):
		body = self.cleaned_data.get('body')
		return body

	layout = Layout('body',)

class EventForm(forms.ModelForm):
	class Meta:
		model = Event
		exclude = ('user',)

class ProjectForm(forms.ModelForm):
	class Meta:
		model = Project
		exclude = ('user',)

class AlumniForm(forms.ModelForm):
	class Meta:
		model = Alumni
		exclude = ('user',)

class MediaForm(forms.ModelForm):
	class Meta:
		model = Media
		exclude = ('user',)
