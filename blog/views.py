from django.shortcuts import render
from django.http import HttpResponse
from django.utils.text import slugify 
from datetime import date

from .models import Author, Post, Tag

list_of_posts = [
  {"name": "Mountain Hiking", "heading":"There's nothing like the views you get when hiking in the mountains", "story":"When i was hiking i saw all sorts of animals and plants", "date":date(2021,7,21), "image": "woods.jpg"},
  {"name": "Programming is great", "heading": "Did you ever spend hours searching that one error in your code", "story": "yadayada", "date": date(2021,8,5), "image":"coding.jpg"},
  {"name": "Nature at its best","heading":"Nature is amazing!","story":"yadayadayada", "date": date(2022,1,10),"image":"mountains.jpg"}
]
latest_posts = list_of_posts

def get_date(post):
    return post['date']

listOfPosts = Post.objects.all()



for post in list_of_posts: # i am using the names in the dictionary here as the urls for our posts, but i have to slugify them with dashes "-" between the words. in a bigger program this would be a function.
    url = slugify(post["name"])
    post["slug"] = url

context = {
    "posts": latest_posts,
} 
# because render requires a dictionary to be passed in, we first have to make a dictionary with a key being how we access the list within the html. 


def index(request):
    sorted_posts = sorted(list_of_posts, key=get_date)
    latest_posts = sorted_posts[-3:]
    return render(request, "blog/index.html", {"posts":listOfPosts})

def posts(request):
    
    
    
    return render(request, "blog/posts.html", {"posts": list_of_posts})

def post(request, post):
    
    for dictionary in list_of_posts:
        if post == dictionary["slug"]:
            postDictionary = dictionary
    return render(request, "blog/post.html", postDictionary)


# Create your views here.
