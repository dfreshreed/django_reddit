"""reddit URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from app.views import index_view, SubredditDetailView, SubpostDetailView, SubCreateView, \
                      SubUpdateView, PostCreateView, UserCreateView, PostUpdateView, \
                      CommentCreateView, CommentUpdateView

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include('django.contrib.auth.urls')),
    url(r'^$', index_view, name='index_view'),
    url('^create_user/$', UserCreateView.as_view(), name="user_create_view"),
    url(r'^subreddit/(?P<pk>\d+)/$', SubredditDetailView.as_view(), name='subreddit_detail_view'),
    url(r'^subpost/(?P<pk>\d+)/$', SubpostDetailView.as_view(), name='subpost_detail_view'),
    url(r'^subadd/$', SubCreateView.as_view(), name='sub_create_view'),
    url(r'^subupdate/(?P<pk>\d+)/$', SubUpdateView.as_view(), name='sub_edit_view'),
    url(r'^subreddit/(?P<pk>\d+)/create/$', PostCreateView.as_view(), name='post_create_view'),
    url(r'^subpost/(?P<pk>\d+)/update/$', PostUpdateView.as_view(), name='post_update_view'),
    url(r'^subpost/(?P<pk>\d+)/create/$', CommentCreateView.as_view(), name='comment_create_view'),
    url(r'^(?P<pk>\d+)/comupdate/$', CommentUpdateView.as_view(), name='comment_update_view'),
]
