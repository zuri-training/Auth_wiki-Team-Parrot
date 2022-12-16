from django.db import models
from django.contrib.auth.models import User
from datetime import datetime


# Create your models here.

GENDER_CHOICES = (
    ('male','MALE'),
    ('female','FEMALE'),
    ('Choose not to say','CHOOSE NOT TO SAY'),
    ('Others','OTHERS'),
    ('Select Gender','SELECT GENDER')
)

class Avatar(models.Model):
    name = models.CharField(max_length=100,blank=False)
    image = models.ImageField(default='profile.jpg', upload_to='profile_pictures', null=False)

    def __str__(self):
        return self.name  


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # image = models.ForeignKey(Avatar, on_delete=models.CASCADE, related_name='avatars')
    # image = forms.ChoiceField(choices = GEEKS_CHOICES)
    created_on = models.DateTimeField(default=datetime.now, blank=True)
    updated_on = models.DateTimeField(default=datetime.now, blank=True)
   
    
    def __str__(self):
        return self.user.username     
        