from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):
    """Post model"""
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(verbose_name='Название поста',max_length=255)
    body = models.TextField(verbose_name='Текст поста')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
