from django.contrib import admin
from .models import Library, CodeSnippet

# Register your models here.
admin.site.register(Library)

@admin.register(CodeSnippet)
class CodeSnippetAdmin(admin.ModelAdmin):
    list_display = ["author", "library", "snippet"]