from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("This Works!")
def posts(request):
    return HttpResponse("This works too!")

def post(request, post):
    
    return HttpResponse("Individual blog post works as well!")


# Create your views here.
