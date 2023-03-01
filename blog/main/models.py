from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import datetime, date
from ckeditor.fields import RichTextField


# Create your models here.
class Posts(models.Model):
    title = models.CharField(
        max_length=255,
    )
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    body = RichTextField(blank=True, null=True)
    created = models.DateField(auto_now_add=True)

    def __str__(self) -> str:
        return self.title + " | " + str(self.author)

    def get_absolute_url(self):
        return reverse("home")
