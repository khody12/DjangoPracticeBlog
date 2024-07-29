from django.shortcuts import render
from django.http import HttpResponse
from django.utils.text import slugify 
from datetime import date

from .models import Author, Post, Tag



list_of_posts = Post.objects.all()


# because render requires a dictionary to be passed in, we first have to make a dictionary with a key being how we access the list within the html. 


def index(request):
    latest_posts = Post.objects.all().order_by("-date")[:3] # this gets the 3 most recent posts, and also

    
    return render(request, "blog/index.html", {"posts":latest_posts})

def posts(request):
    
    return render(request, "blog/posts.html", {"posts": list_of_posts})

def post(request, postName):

    post = list_of_posts.get(slug=postName)

    return render(request, "blog/post.html", {"post":post})


# Create your views here.
