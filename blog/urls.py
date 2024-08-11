from django.urls import path
from . import views

urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),
    path("posts", views.PostsView.as_view(),name="posts"),
    path("posts/<slug:slug>", views.SinglePostView.as_view(),name="post"),
    path("read-later", views.ReadLater.as_view(),name="read-later")
]

