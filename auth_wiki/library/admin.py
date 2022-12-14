from django.contrib import admin
from .models import *

# Register your models here.

admin.site.register(Faq)
admin.site.register(Post)
# admin.site.register(Comment)
admin.site.register(Category)


# from django.contrib import admin
from .models import Post, Comment
@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('user', 'content', 'post', 'created_on')
    list_filter = ('created_on',)
    search_fields = ('user', 'email', 'content')
    actions = ['approve_comments']

    def approve_comments(self, request, queryset):
        queryset.update(active=True)