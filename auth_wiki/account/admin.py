from django.contrib import admin
from .models import Gender, Profile, Comment
# Register your models here.

@admin.register(Gender)
class GenderAdmin(admin.ModelAdmin):
    list_display = ["gender"]

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'first_name', 'last_name']

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['profile', 'comment']
