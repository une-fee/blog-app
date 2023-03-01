from django.urls import path
from .views import UserRegisterView, UserEditView, PasswordChangeView

urlpatterns = [
    path("sign-up/", UserRegisterView.as_view(), name="sign-up"),
    path("edit-profile/", UserEditView.as_view(), name="edit_profile"),
    path("password/", PasswordChangeView.as_view(), name="change-password"),
]
