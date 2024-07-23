from django.shortcuts import render
from django.http import HttpResponse
from django.utils.text import slugify 

list_of_posts = [
  {"name": "Mountain Hiking", "heading":"There's nothing like the views you get when hiking in the mountains", "content":"yadayadayada", },
  {"name": "Programming is great", "heading": "Did you ever spend hours searching that one error in your code", "content": "yadayada"},
  {"name": "Nature at its best","heading":"Nature is amazing!","content":"yadayadayada" }
]
latest_posts = list_of_posts


for post in list_of_posts:
    url = slugify(post["name"])
    post["slug"] = url

context = {
    "posts": latest_posts,
} # because render requires a dictionary to be passed in, we first have to make a dictionary with a key being how we access the list within the html. 


def index(request):
    return render(request, "blog/index.html", context)

def posts(request):
    
    return render(request, "blog/posts.html", context)

def post(request, post):
    
    for dictionary in list_of_posts:
        if post == dictionary["slug"]:
            postDictionary = dictionary
    return render(request, "blog/post.html", postDictionary)




    

    return HttpResponse("Individual blog post works as well!")


# Create your views here.
