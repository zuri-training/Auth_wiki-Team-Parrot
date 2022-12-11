from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from django.forms import ModelForm
from . import views
from .models import *


class NewUserForm(UserCreationForm):
    email = forms.EmailField(required=True, widget=forms.EmailInput(attrs={'class':'focus:outline-none','placeholder':'user@gmail.com'}))
    # username = forms.CharField(required=True, widget=forms.TextInput(attrs={'class':'focus:outline-none','placeholder':'username'}))
    # password1 = forms.CharField(required=True, widget=forms.PasswordInput(attrs={'class':'focus:outline-none'}))
    # password2 = forms.CharField(required=True, widget=forms.PasswordInput(attrs={'class':'focus:outline-none',}))
    
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
        fields=['user','first_name','last_name','gender','image','contact_number'] #'created_on', 'updated_on']
        
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
    image = forms.ImageField(widget=forms.FileInput(attrs={'class': 'form-control-file'}))
    first_name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    gender = forms.ChoiceField(choices= GENDER_CHOICES)
    # bio = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 5}))
    contact_number = forms.CharField(widget=forms.NumberInput(attrs={'class':'form-control'}))
    class Meta:
        model= Profile
        fields = '__all__'