from django.db import models
from django.utils import timezone
from django.contrib.auth import get_user_model
from django.conf import settings
from datetime import datetime
from account.models import *

# Create your models here.

class Post(models.Model):
    title = models.TextField(max_length=500)
    description = models.TextField(max_length=700)
    code_snippet = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    likes= models.IntegerField(default=0)
    dislikes= models.IntegerField(default=0)
    numberofdownloads = models.IntegerField(default=0)
    github = models.URLField(max_length=500, null=True, blank=True,)
    download = models.URLField(max_length=500, null=True, blank=True,)
    images = models.ImageField(upload_to='library_images', blank=True)

    def __str__(self):
        return f'{self.title} <--> {self.author}'

class Category(models.Model):
    name = models.CharField(max_length=200, default="Auth Lib")

    def __str__(self):
        return self.name


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    email = models.EmailField()
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=False)

    class Meta:
        ordering = ['created_on']

    def __str__(self):
        return 'Comment {0} by {1}'.format(self.content, self.user)


class UpVote(models.Model):
    comment = models.ForeignKey(
        Comment, on_delete=models.CASCADE, related_name="upvote_user"
    )
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)

    def __str__(self):
        return str(self.user)


class DownVote(models.Model):
    comment = models.ForeignKey(
        Comment, on_delete=models.CASCADE, related_name="downvote_user"
    )
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE,)

    def __str__(self):
        return str(self.user)


class Faq(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()

    def __str__(self):
        return self.title
