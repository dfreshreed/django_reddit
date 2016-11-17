from django.contrib import admin
from app.models import Subreddit, Post, Comment, Profile


admin.site.register([Subreddit, Post, Comment, Profile])
