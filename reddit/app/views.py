from django.shortcuts import render
from app.models import Subreddit, Post, Comment
from django.views.generic import DetailView, ListView
from django.views.generic.edit import CreateView, UpdateView


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

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["count"] = Subreddit.objects.all()
        return context


class SubpostDetailView(DetailView):
    model = Post

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["count"] = Subreddit.objects.all()
        return context

    def get_comment(self):
        comment = Comment.objects.all()
        return comment
    # for item in Comment.objects.all():
    #     print(item.comment)


class SubCreateView(CreateView):
    model = Subreddit
    success_url = "/"
    fields = ('name', 'description')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["count"] = Subreddit.objects.all()
        return context
