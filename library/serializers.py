from account.models import User
from rest_framework import serializers
from library.models import *





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
    upvote = UpVoteSerializer(many=True, read_only=True)
    downvote = DownVoteSerializer(many=True, read_only=True)

    class Meta:
        model = Comment
        exclude = ('post',)
        fields = ('user', 'content')