from django.contrib import admin

from .models import Post, Like


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    """Posts"""
    list_display = ('title', 'author', 'created_at', 'id')


@admin.register(Like)
class Likedmin(admin.ModelAdmin):
    """Likes"""
    list_display = ('user', 'post', 'like', 'date')
