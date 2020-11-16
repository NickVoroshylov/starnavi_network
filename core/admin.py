from django.contrib import admin

from .models import Post, Like


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    """Posts"""
    list_display = ('title', 'author', 'created_at')
    search_fields = ('title', 'author__username')


@admin.register(Like)
class Likedmin(admin.ModelAdmin):
    """Likes"""
    list_display = ('user', 'post', 'like', 'date')
    list_filter  = ('like',)
    search_fields = ('post_title', 'author__username')
