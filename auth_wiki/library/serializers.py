from rest_framework import serializers
from .models import Post, Comment, DownVote, UpVote


class UpVoteSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField()

    class Meta:
        model = UpVote
        exclude = ('comment',)


class DownVoteSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField()

    class Meta:
        model = DownVote
        exclude = ('comment',)


class CommentSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField()
    upvote_user = UpVoteSerializer(many=True, read_only=True)
    downvote_user = DownVoteSerializer(many=True, read_only=True)

    class Meta:
        model = Comment
        exclude = ('post',)
        fields = ('user', 'content')
