from django.shortcuts import render
from django.views import generic
from .forms import SignUpForm, EditProfileForm
from django.urls import reverse_lazy
from django.contrib.auth.views import PasswordChangeView
from django.contrib.auth.forms import PasswordChangeForm


# Create your views here.
class UserRegisterView(generic.CreateView):
    form_class = SignUpForm
    template_name = "registration/sign-up.html"
    success_url = reverse_lazy("login")


class UserEditView(generic.UpdateView):
    form_class = EditProfileForm
    template_name = "registration/edit_profile.html"
    success_url = reverse_lazy("home")

    def get_object(self):
        return self.request.user


class PasswordChangeView(PasswordChangeView):
    form_class = PasswordChangeForm
    template_name = "registration/change-password.html"
    success_url = reverse_lazy("login")
