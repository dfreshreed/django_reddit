from django.shortcuts import render
from app.models import Subreddit, Post, Comment
from django.views.generic import DetailView, ListView


def index_view(request):
    # for item in Subreddit.objects.all():
    #     print(item.current_count())
    context = {
        "count": Subreddit.objects.all(),
        "time": Subreddit.objects.all(),
        "post": Post.objects.all(),
    }
    return render(request, "index.html", context)


class SubredditDetailView(DetailView):
    model = Subreddit

    # def get_context_data(self):
    #     context = {
    #         "all_posts": Subreddit.objects.all()
    #     }
    #     return context
