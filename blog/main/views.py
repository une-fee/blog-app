from .models import Posts
from .forms import PostForm, EditForm
from django.urls import reverse_lazy
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)


class HomeView(ListView):
    model = Posts
    template_name = "home.html"
    ordering = ["-created"]


class PostDetailView(DetailView):
    model = Posts
    context_object_name = "post"
    template_name = "single_post.html"


class AddPostView(CreateView):
    model = Posts
    form_class = PostForm
    template_name = "add_post.html"


class UpdatePostView(UpdateView):
    model = Posts
    context_object_name = "post"
    form_class = EditForm
    template_name = "update_post.html"


class DeletePostView(DeleteView):
    model = Posts
    context_object_name = "post"
    template_name = "delete_post.html"
    success_url = reverse_lazy("home")
