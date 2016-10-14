from django.db import models
from django.contrib.auth.models import User
import datetime


class Subreddit(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    creation = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    @property
    def current_count(self):
        return Post.objects.filter(subreddit=self).count()

    def today_count(self):
        date = datetime.datetime.now() - datetime.timedelta(days=1)
        return Post.objects.filter(subreddit=self).filter(creation_time__gte=date).count()

    def daily_add(self):
        date7 = datetime.datetime.now() - datetime.timedelta(days=7)
        return Post.objects.filter(subreddit=self).filter(creation_time__gte=date7).count()/7

    @property
    def top_20(self):
        return Post.objects.filter(subreddit=self).order_by("-creation_time")[:21]


class Post(models.Model):
    title = models.CharField(max_length=150)
    description = models.CharField(max_length=255)
    url = models.URLField(null=True, blank=True)
    creation_time = models.DateTimeField(auto_now_add=True)
    modification_time = models.DateTimeField(auto_now=True)
    subreddit = models.ForeignKey(Subreddit)
    user = models.ForeignKey(User)

    def __str__(self):
        return self.title

    def is_recent(self):
        date = datetime.datetime.now() - datetime.timedelta(days=1)
        if Post.objects.filter(creation_time__gte=date):
            return True
        else:
            return False

    def is_hot(self):
        time = datetime.datetime.now() - datetime.timedelta(hours=3)
        if Comment.objects.filter(post=self).filter(created_time__gt=time).count() > 3:
            return True
        else:
            return False

    @property
    def comment(self):
        return Comment.objects.filter(post=self).order_by("-created_time")

    @property
    def count(self):
        return Comment.objects.filter(post=self).count()    

class Comment(models.Model):
    comment = models.TextField(max_length=255)
    user = models.ForeignKey(User)
    post = models.ForeignKey(Post)
    created_time = models.DateTimeField(auto_now_add=True)
    modified_time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.post.title
        return self.comment
