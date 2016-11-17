from django.shortcuts import render
from app.models import Subreddit, Post, Comment, Profile
from django.views.generic import DetailView, ListView
from django.views.generic.edit import CreateView, UpdateView
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse, reverse_lazy


class IndexListView(ListView):
    model = Subreddit
    success_url = '/'

    def get_context_data(self):
        context = super().get_context_data()
        context["count"] = Subreddit.objects.all()
        return context


class UserCreateView(CreateView):
    model = User
    form_class = UserCreationForm
    success_url = "/"


class ProfileDetailView(DetailView):
    model = Profile

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["profile"] = Profile.objects.filter(id=self.kwargs['pk'])
        return context

    def get_success_url(self, **kwargs):
        return reverse_lazy('profile_detail_view', args=[int(self.kwargs['pk'])])


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
    # def get_comment(self):
    #     comment = Comment.objects.all()
    #     return comment
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


class SubUpdateView(UpdateView):
    model = Subreddit
    success_url = "/"
    fields = ('name', 'description')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["count"] = Subreddit.objects.all()
        return context

    # def lazy_url(self, **kwargs):
    #     return reverse('subreddit_detail_view', args=self.kwargs['pk'])


class PostCreateView(CreateView):
    model = Post
    success_url = "/"
    fields = ('title', 'description', 'url')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["count"] = Subreddit.objects.all()
        return context

    def form_valid(self, form):
        instance = form.save(commit=False)
        instance.user = self.request.user
        instance.subreddit = Subreddit.objects.get(id=self.kwargs['pk'])
        return super().form_valid(form)


class PostUpdateView(UpdateView):
    model = Post
    success_url = "/"
    fields = ('title', 'description', 'url')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["count"] = Subreddit.objects.all()
        return context


class CommentCreateView(CreateView):
    model = Comment
    # success_url = "/"
    fields = ('comment',)

    def form_valid(self, form):
        instance = form.save(commit=False)
        instance.user = self.request.user
        instance.post = Post.objects.get(id=self.kwargs['pk'])
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["count"] = Subreddit.objects.all()
        return context

    def get_success_url(self, **kwargs):
        return reverse_lazy('subpost_detail_view', args=[int(self.kwargs['pk'])])


class CommentUpdateView(UpdateView):
    model = Comment
    # success_url = "/"
    fields = ('comment',)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["count"] = Subreddit.objects.all()
        return context

    def get_success_url(self, **kwargs):
        post_id = Comment.objects.get(id=self.kwargs['pk']).post.id
        return reverse('subpost_detail_view', args=[post_id])
