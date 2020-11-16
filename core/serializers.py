from django.contrib.auth.models import User
from rest_framework import serializers

from .models import Like, Post


class PostListSerializer(serializers.ModelSerializer):
    """Post list serializer"""
    author = serializers.SlugRelatedField(slug_field='username', read_only=True)
    likes_count = serializers.SerializerMethodField()
    dislikes_count = serializers.SerializerMethodField()
    # total = serializers.SerializerMethodField()

    class Meta:
        model = Post
        fields = ('author', 'title', 'created_at', 'likes_count', 'dislikes_count')

    def get_likes_count(self, instance):
        return Like.objects.filter(post=instance, like='like').count()
        
    def get_dislikes_count(self, instance):
        return Like.objects.filter(post=instance, like='dislike').count()
        
    # def get_total(self, instance):
    #     likes_f = Like.objects.filter(post=instance, like='like').count()
    #     dislikes_f = Like.objects.filter(post=instance, like='dislike').count()
    #     return {"likes": likes_f, 'dislikes': dislikes_f}



class PostDetailSerializer(serializers.ModelSerializer):
    """Detail post serializer"""
    author = serializers.SlugRelatedField(slug_field='username', read_only=True)

    class Meta:
        model = Post
        fields = '__all__'


class PostCreateSerializer(serializers.ModelSerializer):
    """Create post serializer"""

    class Meta:
        model = Post
        fields = ('author', 'title', 'body', 'created_at')


class LikeCreateSerializer(serializers.ModelSerializer):
    """Like post serializer"""

    class Meta:
        model = Like
        fields = ('user', 'post', 'like', 'date')

    def create(self, validated_data):
        like, _ = Like.objects.update_or_create(
            user=validated_data.get('user', None),
            post=validated_data.get('post', None),
            defaults={'like': validated_data.get('like')}
        )
        return like
        

class LikeListSerializer(serializers.ModelSerializer):
    """Post list serializer"""
    user = serializers.SlugRelatedField(slug_field='username', read_only=True)
    post = serializers.SlugRelatedField(slug_field='title', read_only=True)

    class Meta:
        model = Like
        fields = ('post', 'user', 'like', 'date')


class UserActivitySerializer(serializers.ModelSerializer):
    """User activity serializer"""

    class Meta:
        model = User
        fields = ('username', 'last_login')
