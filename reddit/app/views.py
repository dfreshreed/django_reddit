from django.shortcuts import render
from app.models import Subreddit, Post, Comment


def index_view(request):
    # for item in Subreddit.objects.all():
    #     print(item.current_count())
    context = {
        "count": Subreddit.objects.all(),
        "time": Subreddit.objects.all()
    }
    return render(request, "index.html", context)
