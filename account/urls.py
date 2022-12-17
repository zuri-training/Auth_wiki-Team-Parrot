# from django.urls import path 
# from account.views import *

# urlpatterns = [
#     path('signup/', signup_view, name='signup'),
#     path('email/', email_view, name='email'),
#     path('forgotpassword/', forgotpassword_view, name='forgotpassword'),

# ]

from django.contrib import admin
from django.urls import path
#from django.urls import include
from . import views
from django.contrib.auth import views as authentication_views



app_name = 'account'
urlpatterns = [
    path('', views.home, name='home'),
    path('register/',views.register, name='register'),
    
    path('login/', views.userlogin, name='login'),
    #path("logout", views.userlogout, name= "logout"),
    
    # path("login/",authentication_views.LoginView.as_view(template_name='users/login.html'),name='login'),
    path('logout/', views.userlogout, name='logout'),
    
    #path("logout/",authentication_views.LogoutView.as_view(template_name='account/logout.html'),name='logout'),
    
    path('profile/', views.profile, name='profile'),
    
    path('updateprofile/', views.Editprofile, name='createprofile'),
    path("password_reset", views.password_reset_request, name="password_reset")

    
    
]