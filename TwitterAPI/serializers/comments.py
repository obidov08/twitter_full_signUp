from django.forms import fields
from rest_framework import serializers
from TwitterAPI.models.comments import Comments
from TwitterAPI.serializers.users import FullSignUpSerializer
from TwitterAPI.serializers.posts import PostCreatedSerializer

class CommentSerializer(serializers.ModelSerializer):
    author = FullSignUpSerializer(source='user', read_only=True)

    class Meta:
        model = Comments
        fields = ['id', 'author', 'post', 'parent', 'text', 'created_at', 'updated_at']
        read_only_fields = ['user', 'created_at', 'updated_at']

    def create(self, validated_data):
        user = self.context['request'].user
        validated_data['user'] = user
        return super().create(validated_data)
    
