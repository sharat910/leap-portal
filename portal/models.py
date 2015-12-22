from django.db import models
from django.contrib.auth.models import User
from .validators import validate_file_extension
# Create your models here.

class Puser(models.Model):
	orgname = models.CharField(max_length=100)
	email = models.EmailField()
	joineddate = models.DateField(auto_now_add = True)
	user = models.OneToOneField(User)
	location = models.CharField(max_length=100)
	designation = models.CharField(max_length=200)
	institution = models.CharField(max_length=200)

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
		return self.pk

class Post(models.Model):
	body = models.CharField(max_length=5000)
	user = models.ForeignKey(Puser)
	created = models.DateTimeField(auto_now_add=True)

	class Meta:
		verbose_name = 'Post'
		verbose_name_plural = 'Posts'
		ordering = ["-created"]
	def __unicode__(self):
		return self.pk


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
	startdate = models.DateField()
	enddate = models.DateField()
	user = models.ForeignKey(Puser)
	details = models.FileField(upload_to="documents/%Y/%m/%d", validators=[validate_file_extension])
