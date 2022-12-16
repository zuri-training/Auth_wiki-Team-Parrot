from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from django.forms import ModelForm
from . import views
from .models import *


class NewUserForm(UserCreationForm):
    email = forms.EmailField(required=True, widget=forms.EmailInput(attrs={'class':'focus:outline-none','placeholder':'user@gmail.com'}))
  
    class Meta:
        model=User
        fields=["username","email","password1","password2"]

    
    def save(self, commit=True):
        user=super(NewUserForm,self).save(commit=False)
        user.email= self.cleaned_data['email']
        if commit:
            user.save()
        return user
    
class ProfileForm(ModelForm):
    class Meta:
        model= Profile
        # fields=['user','image']
        fields=['user']
        
class UpdateUserForm(ModelForm):
    username = forms.CharField(max_length=100,
                               required=True,
                               widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(required=True,
                             widget=forms.EmailInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ['username', 'email']


class UpdateProfileForm(ModelForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    image = forms.ImageField(widget=forms.FileInput(attrs={'class': 'form-control-file'}))
   
    class Meta:
        model= Profile
        fields = '__all__'