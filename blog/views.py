from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import (
    ListView, DetailView, CreateView, UpdateView, DeleteView
)
from .models import Post


# class-based views
def home(request):
    contex = {
        'posts': Post.objects.all()
    }
    # to add html template:
    return render(request, 'blog/home.html', contex)


class PostListView(ListView):
    model = Post
    # create new template
    # default path: <app>/<model>_<viewtype>.html
    template_name = 'blog/home.html'
    context_object_name = 'posts'
    # to change order of posts
    ordering = ['-date_posted']


class PostDetailView(DetailView):
    model = Post


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

# mixin to valid if the user is the author of the post


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    # function to check if the user try too edit his own post
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    # to redirect to homepage after delete post:
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

# simple pass dictionary as argument to set title in about pages


def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})
