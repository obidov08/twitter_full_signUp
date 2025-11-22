from rest_framework.serializers import ModelSerializer
from django.forms import fields
from rest_framework import serializers
from TwitterAPI.models.like import PostLike, CommentLike
from TwitterAPI.serializers.users import FullSignUpSerializer

class PostLikeSerializer(serializers.ModelSerializer):
    user = FullSignUpSerializer(read_only=True)

    class Meta:
        model = PostLike
        fields = ['id', 'user', 'post', 'is_like', 'created_at']
        read_only_fields = ['user']


class CommentLikeSerializer(serializers.ModelSerializer):
    user = FullSignUpSerializer(read_only=True)

    class Meta:
        model = CommentLike
        fields = ['id', 'user', 'comment', 'is_like', 'created_at']
        read_only_fields = ['user']

        