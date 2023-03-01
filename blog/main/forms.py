from django import forms
from .models import Posts


class PostForm(forms.ModelForm):
    class Meta:
        model = Posts
        fields = ["title", "author", "body"]

        widgets = {
            "title": forms.TextInput(attrs={"class": "form-control"}),
            "author": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "value": "",
                    "id": "elder",
                    "type": "hidden",
                }
            ),
            "body": forms.Textarea(
                attrs={"class": "form-control", "placeholder": "Put you're text here"}
            ),
        }


class EditForm(forms.ModelForm):
    class Meta:
        model = Posts
        fields = ["title", "body"]

        widgets = {
            "title": forms.TextInput(attrs={"class": "form-control"}),
            "body": forms.Textarea(
                attrs={"class": "form-control", "placeholder": "Put you're text here"}
            ),
        }
