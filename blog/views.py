from django.shortcuts import render
from django.http import HttpResponse
from django.utils.text import slugify 
from datetime import date

from .models import Author, Post, Tag



listOfPosts = Post.objects.all()


# because render requires a dictionary to be passed in, we first have to make a dictionary with a key being how we access the list within the html. 


def index(request):
    
    return render(request, "blog/index.html", {"posts":listOfPosts})

def posts(request):
    
    return render(request, "blog/posts.html", {"posts": listOfPosts})

def post(request, postName):

    post = listOfPosts.get(slug=postName)

    return render(request, "blog/post.html", {"post":post})


# Create your views here.
