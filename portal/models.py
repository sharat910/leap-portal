from django.db import models
from django.contrib.auth.models import User
from .validators import validate_file_extension, validate_file_extension_intro 
# Create your models here.

class Puser(models.Model):
	orgname = models.CharField(max_length=100)
	image = models.FileField(upload_to='images/%Y/%m/%d',blank=False)
	email = models.EmailField()
	joineddate = models.DateField(auto_now_add = True)
	user = models.OneToOneField(User)
	location = models.CharField(max_length=100)
	#designation = models.CharField(max_length=200,blank = True,null = True)
	institution = models.CharField(max_length=200)
	contact = models.IntegerField()
	weblink = models.CharField(max_length=200,null = True,blank = True)
	fbprofile = models.CharField(max_length=200,null = True,blank = True)
	introduction = models.FileField(upload_to='intros/',	validators = [validate_file_extension_intro],null = True ,blank=True)



	def __unicode__(self):
		return self.orgname

class Query(models.Model):
	body = models.CharField(max_length=5000)
	user = models.ForeignKey(Puser)
	created = models.DateTimeField(auto_now_add=True)

	class Meta:
		verbose_name = 'Query'
		verbose_name_plural = 'Queries'
		ordering = ["-created"]

	def __unicode__(self):
		return self.body

	def get_answers(self):
		return self.answer_set.all()

class Post(models.Model):
	body = models.CharField(max_length=5000)
	user = models.ForeignKey(Puser)
	created = models.DateTimeField(auto_now_add=True)

	class Meta:
		verbose_name = 'Post'
		verbose_name_plural = 'Posts'
		ordering = ["-created"]
	def __unicode__(self):
		return self.body

	def get_comments(self):
		return self.comment_set.all()

class Comment(models.Model):
	post = models.ForeignKey(Post)
	body = models.TextField(null = False)
	user = models.ForeignKey(Puser)
	created = models.DateTimeField(auto_now_add=True)

	def __unicode__(self):
		return self.body

	class Meta:
		ordering = ["-created"]

class Answer(models.Model):
	query = models.ForeignKey(Query)
	body = models.TextField(null = False)
	user = models.ForeignKey(Puser)
	created = models.DateTimeField(auto_now_add=True)

	def __unicode__(self):
		return self.body

	class Meta:
		ordering = ["-created"]

class Event(models.Model):
	name = models.CharField(max_length=100)
	description = models.TextField()
	user = models.ForeignKey(Puser)
	created = models.DateTimeField(auto_now_add=True)
	details = models.FileField(upload_to="documents/%Y/%m/%d", validators=[validate_file_extension], null = True,blank=True)

	def __unicode__(self):
		return self.name

	class Meta:
		ordering = ["-created"]

class Project(models.Model):
	name = models.CharField(max_length=100)
	description = models.TextField()
	user = models.ForeignKey(Puser)
	teamstrength = models.IntegerField()
	workingarea = models.CharField(max_length=200)
	achievements = models.TextField(null = True, blank = True)
	details = models.FileField(upload_to="documents/%Y/%m/%d", validators=[validate_file_extension],null = True,blank=True)
	created = models.DateTimeField(auto_now_add=True)

	def __unicode__(self):
		return self.name

	class Meta:
		ordering = ["-created"]

class Alumni(models.Model):
	name = models.CharField(max_length=100)
	about = models.TextField()
	user = models.ForeignKey(Puser)
	created = models.DateTimeField(auto_now_add=True)

	def __unicode__(self):
		return self.name

class Media(models.Model):
	title = models.CharField(max_length=100)
	link = models.TextField(blank=True)
	description = models.TextField()
	user = models.ForeignKey(Puser)
	created = models.DateTimeField(auto_now_add=True)

	def __unicode__(self):
		return self.title
