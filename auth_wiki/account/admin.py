from django.contrib import admin
from .models import Profile

# Register your models here.
admin.site.register(Profile)
                    
                    
class AccountAdmin(admin.ModelAdmin):
    list_display = ('user','first_name','last_name','gender',)
    search_fields = ('user',)