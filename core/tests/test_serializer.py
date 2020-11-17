from django.contrib.auth.models import User
from django.test import TestCase

from core.models import Post
from core.serializers import PostListSerializer


class PostListSerializerTestCase(TestCase):
    def test_ok(self):
        user = User.objects.create_user(username='testuser', password='12345')
        post_1 = Post.objects.create(author=user, title='Test post 1',
                                     body='Test body')
        post_2 = Post.objects.create(author=user, title='Test post 2',
                                     body='Test body 2')
        data = PostListSerializer([post_1, post_2], many=True).data
        expected_data = [
            {
                'author': user.username,
                'title': 'Test post 1',
                'created_at': '2020-11-16',
                'likes_count': 0,
                'dislikes_count': 0
            },
            {
                'author': user.username,
                'title': 'Test post 2',
                'created_at': '2020-11-16',
                'likes_count': 0,
                'dislikes_count': 0
            }
        ]
        self.assertEqual(expected_data, data)
