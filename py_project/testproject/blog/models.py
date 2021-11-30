from django.db import models
from django.contrib.auth.models import User

class Page(models.Model):

    unique_name = models.CharField(max_length=64, unique=True)

    title = models.CharField(max_length=128)
    content = models.TextField(blank=True)

class Post(models.Model):
    title = models.CharField(max_length=128)
    content = models.TextField(blank=True)

    author = models.ForeignKey(User, on_delete=models.CASCADE,
        blank=True, null=True,
    )
