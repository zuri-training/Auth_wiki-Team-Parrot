from django.urls import path 
from library.views import *

app_name = 'library'
urlpatterns = [
    path('', home_view, name='home'),
    path('about/', about_view, name='about'),
    path('faq/', faq_view, name='faq'),
    path('library/', library_view, name='library'),
    path("<int:pk>/create_comment", CommentAPIView.as_view(), name="create-comment"),
    path("comment/<int:pk>/create_upvote", UpVoteAPIView.as_view(), name="create-upvote"),
    path("comment/<int:pk>/create_downvote", DownVoteAPIView.as_view(), name="create-downvote")
]