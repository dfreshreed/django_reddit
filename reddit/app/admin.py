from django.contrib import admin
from app.models import Subreddit, Post, Comment


admin.site.register([Subreddit, Post, Comment])
