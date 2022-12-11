from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from django.forms import ModelForm
from . import views
from . import models


class NewUserForm(UserCreationForm):
    email = forms.EmailField(required=True, widget=forms.EmailInput(attrs={'class':'focus:outline-none','placeholder':'user@gmail.com'}))
    # username = forms.CharField(required=True, widget=forms.TextInput(attrs={'class':'focus:outline-none','placeholder':'username'}))
    # password1 = forms.CharField(required=True, widget=forms.PasswordInput(attrs={'class':'focus:outline-none'}))
    # password2 = forms.CharField(required=True, widget=forms.PasswordInput(attrs={'class':'focus:outline-none',}))
    
    class Meta:
        model=User
        fields=("username","email","password1","password2")

    
    def save(self, commit=True):
        user=super(NewUserForm,self).save(commit=False)
        user.email= self.cleaned_data['email']
        if commit:
            user.save()
        return user
    
class ProfileForm(ModelForm):
    class Meta:
        model= models.Profile
        fields=['user','first_name','last_name','gender','image','contact_number'] #'created_on', 'updated_on']
    
    
    
    
    