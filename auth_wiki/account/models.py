from django.db import models
from django.contrib.auth.models import User
#from django.utils.timezone import datetime
from datetime import datetime

# Create your models here.

GENDER_CHOICES = (
    ('male','MALE'),
    ('female','FEMALE'),
    ('Choose not to say','CHOOSE NOT TO SAY'),
    ('Others','OTHERS'),
    ('Select Gender','SELECT GENDER')
)
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=50, default='SOME STRING')
    last_name = models.CharField(max_length=50, default='SOME STRING')
    gender=models.CharField(max_length=30, choices=GENDER_CHOICES, default='Select Gender')
    image = models.ImageField(default='profile.jpg',upload_to='profile_pictures')
    contact_number = models.CharField(max_length=100, default='00000000000')
    created_on = models.DateTimeField(default=datetime.now, blank=True)
    updated_on = models.DateTimeField(default=datetime.now, blank=True)
    #, null=True
    
    def __str__(self):
        return self.user.username
        
    