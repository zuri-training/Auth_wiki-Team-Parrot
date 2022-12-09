from django.shortcuts import render
from rest_framework import generics
from rest_framework.authentication import TokenAuthentication
from rest_framework.exceptions import ValidationError
from rest_framework.permissions import IsAdminUser, IsAuthenticated

from .models import Post, Comment, DownVote, UpVote
from .serializers import (
    PostSerializer,
    CommentSerializer,
    DownVoteSerializer,
    UpVoteSerializer,
)

# Create your views here.
class DownVoteAPIView(generics.CreateAPIView):
    serializer_class = DownVoteSerializer
    queryset = DownVote.objects.all()
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        pk = self.kwargs["pk"]
        comment = Comment.objects.get(pk=pk)
        review_user = self.request.user
        upvote_queryset = UpVote.objects.filter(comment=comment, user=review_user)
        downvote_queryset = DownVote.objects.filter(comment=comment, user=review_user)
        if downvote_queryset.exists():
            raise ValidationError("Comment already downvoted by you")
        if upvote_queryset.exists():
            upvote_queryset.delete()
        serializer.save(comment=comment, user=review_user,)


class UpVoteAPIView(generics.CreateAPIView):
    serializer_class = UpVoteSerializer
    queryset = UpVote.objects.all()
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        pk = self.kwargs["pk"]
        comment = Comment.objects.get(pk=pk)
        review_user = self.request.user
        upvote_queryset = UpVote.objects.filter(comment=comment, user=review_user)
        downvote_queryset = DownVote.objects.filter(comment=comment, user=review_user)
        if upvote_queryset.exists():
            raise ValidationError("Comment already upvoted by you")
        if downvote_queryset.exists():
            downvote_queryset.delete()
        serializer.save(comment=comment, user=review_user,)


class CommentAPIView(generics.ListCreateAPIView):
    serializer_class = CommentSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Comment.objects.all()

    def get_object(self):
        return Comment.objects.all()

    def perform_create(self, serializer):
        pk = self.kwargs["pk"]
        post = Post.objects.get(pk=pk)
        user = self.request.user
        serializer.save(**self.request.data, user=user, post=post)

