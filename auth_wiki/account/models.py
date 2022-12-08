from django.db import models
from django.contrib.auth.models import User
from  library.models import CodeSnippet

# Create your models here.
class Gender(models.Model):
    gender = models.CharField(max_length=10)

    def __str__(self):
        return self.gender

class Profile(models.Model):
    user =  models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    gender = models.ForeignKey(Gender, on_delete=models.PROTECT)
    created_at = models.DateField(auto_now_add=True)
    updaated_at = models.DateField(auto_now=True)
    
    def __str__(self): 
        return f"{self.first_name} {self.last_name}"

class Comment(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    code_snippet = models.ForeignKey(CodeSnippet, on_delete=models.CASCADE)
    comment = models.TextField()
    img_url = models.URLField()
    created_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.comment
