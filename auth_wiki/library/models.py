from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Library(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class CodeSnippet(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    library = models.ForeignKey(Library, on_delete=models.CASCADE)
    snippet = models.TextField()
    example = models.TextField()
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    def __str__(self):
        return self.snippet
    