from django.urls import path 
from library.views import *
from . import views

app_name = 'library'
urlpatterns = [
    path('',views.home, name="home"),
]