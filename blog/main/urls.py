from django.urls import path
from .views import HomeView, PostDetailView, AddPostView, UpdatePostView, DeletePostView

urlpatterns = [
    path("", HomeView.as_view(), name="home"),
    path("post/<int:pk>", PostDetailView.as_view(), name="single_post"),
    path("add-post", AddPostView.as_view(), name="add_post"),
    path("post/edit-post/<int:pk>", UpdatePostView.as_view(), name="update_post"),
    path("post/delete-post/<int:pk>", DeletePostView.as_view(), name="delete_post"),
]
