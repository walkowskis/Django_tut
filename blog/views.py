from django.shortcuts import render
from .models import Post


def home(request):
    contex = {
        'posts': Post.objects.all()
    }
    # to add html template:
    return render(request, 'blog/home.html', contex)

# simple pass dictionary as argument to set title in about pages


def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})
