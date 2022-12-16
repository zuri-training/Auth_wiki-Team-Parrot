from django.shortcuts import render, get_object_or_404
from .models import *
from .forms import *
from .serializers import *
from django.http import HttpResponseRedirect
from django.urls import reverse
from rest_framework import generics
from rest_framework.authentication import TokenAuthentication
from rest_framework.exceptions import ValidationError
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from django.contrib.auth.decorators import login_required
from django.db.models.query_utils import Q


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


def documentation_view(request):
    template_name = 'main/documentation.html'
    context = {}
    return render(request, template_name, context=context)



@login_required(login_url='account:register')
def detail_view(request, slug):
    template_name = 'main/details_page.html'
    requested_post = get_object_or_404(Post, slug=slug)
    comments = requested_post.comments.all().order_by('-created_on')
    form = CommentForm()
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = requested_post
            comment.user = request.user
            comment.save()
            return HttpResponseRedirect(reverse('details', args=[slug]))



    context = {
        'detail_post': requested_post,
        'comments_data': comments,
        'comment_form': form,
    }

    return render(request, template_name, context)


def search_library(request):
    search_q = request.GET.get('q')
    filtered_object = Post.objects.filter(Q(title__contains=search_q) | Q(description__contains=search_q))
    context = {
        'post_data': filtered_object,
        'length_of_data': len(filtered_object),
        'searched_q': search_q,
    }
    return render(request, 'main/search.html', context)
    



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
