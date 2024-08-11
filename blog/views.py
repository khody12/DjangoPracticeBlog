from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.utils.text import slugify 
from datetime import date

from .models import Author, Post, Tag, Comment
from .forms import CommentForm
from django.views import View
from django.views.generic import DetailView, ListView




list_of_posts = Post.objects.all()


# because render requires a dictionary to be passed in, we first have to make a dictionary with a key being how we access the list within the html. 


class IndexView(ListView):
    template_name = "blog/index.html"
    model = Post
    context_object_name = "posts"

    def get_queryset(self, **kwargs):
        base_query = super().get_queryset()
        data = base_query.order_by("-date")[:3]
        return data


# def index(request):
#     latest_posts = Post.objects.all().order_by("-date")[:3] # this gets the 3 most recent posts, and also
#     latest_posts = Post.objects.all().filter()

    
#     return render(request, "blog/index.html", {"posts":latest_posts})
class PostsView(ListView):
    template_name = "blog/posts.html"
    model = Post
    context_object_name = "posts"


# def posts(request):
    
#     return render(request, "blog/posts.html", {"posts": list_of_posts})


class SinglePostView(DetailView):
    template_name = "blog/post.html"
    model = Post

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = CommentForm()
        return context



    def post(self, request, *args, **kwargs):
        self.object = self.get_object() # i am basically getting ourself in this function. im getting the post object. 
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = Comment(post=self.object, comment=form.cleaned_data['comment']) # 'comment' is the variable we are accessing from the form.
            comment.save() # saving this comment object to our database.

            return redirect("post", self.object.slug) # redirect works by taking the name from the urls.py of the template we want to navigate to, and then
             # we pass in the slug ourselves, because we have access to our own object. 

class ReadLater(View):
    pass

        
    




# # def post(request, postName):

# #     if request.method == "POST":
# #         form = CommentForm(request.POST)

# #         if form.is_valid():
# #             comment = Comment(comment=form.cleaned_data['comment'])
# #             comment.save()
# #             return redirect('post',slug=postName)
# #     else:
# #         form = CommentForm()

    


#     post = list_of_posts.get(slug=postName)

#     return render(request, "blog/post.html", {
#         "post":post,
#         "post_tags": post.caption.all(),
#         "form":form
#         })


    


# Create your views here.
