from django.urls import path, include
from rest_framework.routers import routers
from . import views
from library.views import CommentAPIView, UpVoteAPIView, DownVoteAPIView


router = routers.DefaultRouter()
router.register(r'comment', views.CommentAPIView, basename="comment")
router.register(r'upvote', views.UpVoteAPIView, basename="upvote")
router.register(r'downvote', views.DownVoteAPIView, basename="downvote")

urlpatterns = [
    path("", include(router.urls)),
    path('api_auth/', include('rest_framework.urls', namespace='rest_framework')),
    path("<int:pk>/create_comment", CommentAPIView.as_view(), name="create-comment"),
    path("comment/<int:pk>/create_upvote", UpVoteAPIView.as_view(), name="create-upvote"),
    path("comment/<int:pk>/create_downvote", DownVoteAPIView.as_view(), name="create-downvote"),
]
