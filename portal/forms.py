from django import forms
from django.contrib.auth.models import User
from django.forms import ModelForm
from .models import *
from material import *
from django.utils.translation import ugettext_lazy as _

class RegistrationForm(ModelForm):
	username = forms.CharField(label = (u'Username'))
	password = forms.CharField(label = (u'Password'), widget = forms.PasswordInput(render_value = False))

	class Meta:
		model = Puser
		exclude = ('user','joineddate','designation',)
		labels = {
            'orgname': _('Organisation Name'),
			'email': _('Email'),
			'weblink': _('Link to your Website'),
			'fbprofile':_('Link to your Facebook Page'),
			'image': _('Logo/DP')
        }



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
	body = forms.CharField(label=(u'Post something happening!'), required = True,widget=forms.Textarea)

	class Meta:
		model = Post
		fields = ['body']

	def clean_body(self):
		body = self.cleaned_data.get('body')
		return body


class QueryForm(forms.ModelForm):
	body = forms.CharField(label=(u'Got a question, shoot it!'), required = True,widget=forms.Textarea)


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
		labels = {
            'name': _('Name of the Event'),
			'details': _('Attach related document in pdf, docx or doc format'),
		}

class ProjectForm(forms.ModelForm):
	class Meta:
		model = Project
		exclude = ('user',)
		labels = {
            'name': _('Name of the Project'),
			'details': _('Attach related document in pdf, docx or doc format'),
		}

class AlumniForm(forms.ModelForm):
	class Meta:
		model = Alumni
		exclude = ('user',)
		labels = {
            'name': _('Name of the Alumnus'),
			'about': _('About Him/Her'),
		}

class MediaForm(forms.ModelForm):
	class Meta:
		model = Media
		exclude = ('user',)
