from django.shortcuts import render
from .models import *
from .serializers import *
from rest_framework import generics
from rest_framework.authentication import TokenAuthentication
from rest_framework.exceptions import ValidationError
from rest_framework.permissions import IsAdminUser, IsAuthenticated
# # testing testing
# from django.shortcuts import render, get_object_or_404, redirect
# from library.models import *
# from account.models import Profile
# from django.http import HttpResponseRedirect
# from account.models import User
# from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
# from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
# from django.db.models import Count
# from .forms import NewCommentForm
# from django.contrib.auth.decorators import login_required

# testing 1..2


# Create your views here.
def home_view(request):
    template_name = 'main/index.html'
    context = {}

    return render(request, template_name)

def about_view(request):
    template_name = 'main/about.html'
    context = {}

    return render(request, template_name)

def faq_view(request):
    template_name = 'main/faq.html'
    data = Faq.objects.all()
    context = {
        'faq_data': data,
    }

    return render(request, template_name, context=context)


def library_view(request):
    template_name = 'main/library.html'
    data = Post.objects.all()
    context = {'post_data':data}
    return render(request, template_name, context=context)



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


# class CommentAPIView(generics.ListCreateAPIView):
#     serializer_class = CommentSerializer
#     authentication_classes = [TokenAuthentication]
#     permission_classes = [IsAuthenticated]
#     queryset = Comment.objects.all()

#     def get_object(self):
#         return Comment.objects.all()

#     def perform_create(self, serializer):
#         pk = self.kwargs["pk"]
#         post = Post.objects.get(pk=pk)
#         user = self.request.user
#         serializer.save(**self.request.data, user=user, post=post)


from .models import Post
from .forms import CommentForm
from django.shortcuts import render, get_object_or_404

def post_detail(request, slug):
    template_name = 'library.html'
    post = get_object_or_404(Post, slug=slug)
    comments = post.comments.filter(active=True)
    new_comment = None
    # Comment posted
    if request.method == 'POST':
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():

            # Create Comment object but don't save to database yet
            new_comment = comment_form.save(commit=False)
            # Assign the current post to the comment
            new_comment.post = post
            # Save the comment to the database
            new_comment.save()
    else:
        comment_form = CommentForm()

    data_user = {'post': post,
            'comments': comments,
            'new_comment': new_comment,
            'comment_form': comment_form}

    return render(request, template_name, data_user=data_user)