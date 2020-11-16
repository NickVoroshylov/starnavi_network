from django.db import models
from django.contrib.auth.models import User

from datetime import date


class Post(models.Model):
    """Post model"""
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(verbose_name='Название поста', max_length=255)
    body = models.TextField(verbose_name='Текст поста')
    created_at = models.DateTimeField(verbose_name='Дата создания поста', auto_now_add=True)

    def __str__(self):
        return self.title


class Like(models.Model):
    """Like model"""
    LIKE = (
        ('like', 'like'),
        ('dislike', 'dislike')
    )

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    like = models.CharField(max_length=255, choices=LIKE)
    date = models.DateField(auto_now=True)

    def __str__(self):
        return self.like
