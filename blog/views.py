from django.shortcuts import render

# Create your views here.

posts = [
    {
        'author': 'Zafar',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'June 20, 2019'
    },
{
        'author': 'John Doe',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'July 22, 2019'
    },
]

def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})