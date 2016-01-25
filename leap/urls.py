"""leap URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url, patterns
from django.contrib import admin
from portal.models import *
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = patterns('portal.views',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^register/$','PuserRegistration'),
    url(r'^login/$','LoginRequest'),
    url(r'^logout/$','LogoutRequest'),
    url(r'^$','StartPage'),
    url(r'^home/$','PostsView'),
    url(r'^queries/$','QueriesView'),
    url(r'^myqueries/$','MyQueriesView'),
    url(r'^search/$','SearchQueriesView'),
    url(r'^comment/$','CommentView'),
    url(r'^answer/$','AnswerView'),
    url(r'^addevent/$','EventView'),
    url(r'^addproject/$','ProjectView'),
    url(r'^addalumnus/$','AlumniView'),
    url(r'^addmedia/$','MediaView'),
    url(r'^profile/(?P<username>\w+)$','ProfileView'),
    url(r'^editprofile/(?P<username>\w+)$','EditProfileView'),
    url(r'^community/$','CommunityView'),
    url(r'^mentors/$','MentorView'),
    url(r'^editpost/(?P<id>\d+)$','EditPostView'),
    url(r'^editquery/(?P<id>\d+)$','EditQueryView'),
    url(r'^editevent/(?P<id>\d+)$','EditEventView'),
    url(r'^editproject/(?P<id>\d+)$','EditProjectView'),



)+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += patterns('',
        (r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT, 'show_indexes': True}),
    )
