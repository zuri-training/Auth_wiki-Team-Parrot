from django.contrib import admin
from .models import Comment, DownVote, UpVote

# Register your models here.
admin.site.register(Comment)
admin.site.register(DownVote)
admin.site.register(UpVote)