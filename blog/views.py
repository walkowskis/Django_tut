from django.shortcuts import render

# some data, as dictionaries:
posts = [
    {
        'author': 'Typ',
        'title': 'Blog post 1',
        'content': 'Random stuff bleee',
        'date_posted': '01.01.2019'
    },
    {
        'author': 'Typ2',
        'title': 'Blog post 2',
        'content': 'Random stuff bleee bleee',
        'date_posted': '01.02.2019'
    }
]

# Create your views here.


def home(request):
    contex = {
        'posts': posts
    }
    # to add html template:
    return render(request, 'blog/home.html', contex)

# simple pass dictionary as argument to set title in about pages


def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})
