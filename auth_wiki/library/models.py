from django.db import models
from django.contrib.auth import get_user_model
from django.conf import settings
from datetime import datetime

# Create your models here.
User = settings.AUTH_USER_MODEL

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
