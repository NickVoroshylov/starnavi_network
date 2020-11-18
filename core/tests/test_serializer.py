from django.contrib.auth.models import User
from django.test import TestCase

from core.models import Like, Post
from core.serializers import (LikeCreateSerializer, LikeListSerializer,
                              PostCreateSerializer, PostDetailSerializer,
                              PostListSerializer)


class PostListSerializerTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.post_1 = Post.objects.create(author=self.user, title='Test post 1',
                                          body='Test body')
        self.post_2 = Post.objects.create(author=self.user, title='Test post 2',
                                          body='Test body 2')
        self.like_1 = Like.objects.create(user=self.user, post=self.post_1,
                                          like='like')

    def test_ok(self):
        data = PostListSerializer([self.post_1, self.post_2], many=True).data
        expected_data = [
            {
                "author": self.user.username,
                "title": self.post_1.title,
                "created_at": self.post_1.created_at.strftime('%Y-%m-%d'),
                "likes_count": 1,
                "dislikes_count": 0
            },
            {
                "author": self.user.username,
                "title": self.post_2.title,
                "created_at": self.post_2.created_at.strftime('%Y-%m-%d'),
                "likes_count": 0,
                "dislikes_count": 0
            }
        ]
        self.assertEqual(expected_data, data)


class PostDetailSerializerTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.post_1 = Post.objects.create(author=self.user, title='Test post 1',
                                          body='Test body')
        self.post_2 = Post.objects.create(author=self.user, title='Test post 2',
                                          body='Test body 2')
        self.like_1 = Like.objects.create(user=self.user, post=self.post_1,
                                          like='like')

    def test_ok(self):
        data = PostDetailSerializer(self.post_1).data
        expected_data = {
                "id": self.post_1.id,
                "author": self.user.username,
                "title": self.post_1.title,
                "body": self.post_1.body,
                "created_at": self.post_1.created_at.strftime('%Y-%m-%d')
            }
        self.assertEqual(expected_data, data)


class PostCreateSerializerTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.post_1 = Post.objects.create(author=self.user, title='Test post 1',
                                          body='Test body')
        self.post_2 = Post.objects.create(author=self.user, title='Test post 2',
                                          body='Test body 2')

    def test_ok(self):
        data = {
            "author": self.user,
            "title": "Post for creating",
            "body": "Text writed for this post"
        }
        serialized_data = PostCreateSerializer(data).data
        expected_data = {
            "author": 1,
            "title": "Post for creating",
            "body": "Text writed for this post"
        }
        self.assertEqual(expected_data, serialized_data)


class LikeCreateSerializerTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.post_1 = Post.objects.create(author=self.user, title='Test post 1',
                                          body='Test body')
        self.post_2 = Post.objects.create(author=self.user, title='Test post 2',
                                          body='Test body 2')
        self.like_1 = Like.objects.create(user=self.user, post=self.post_1,
                                          like='like')

    def test_ok(self):
        data = {
            "user": self.user,
            "post": self.post_2,
            "like": "dislike"
        }
        serialized_data = LikeCreateSerializer(data).data
        expected_data = {
            "user": 1,
            "post": 2,
            "like": "dislike"
        }
        self.assertEqual(expected_data, serialized_data)


class LikeListSerializerTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.post_1 = Post.objects.create(author=self.user, title='Test post 1',
                                          body='Test body')
        self.post_2 = Post.objects.create(author=self.user, title='Test post 2',
                                          body='Test body 2')
        self.post_3 = Post.objects.create(author=self.user, title='Test post 3',
                                          body='Test body 3')              
        self.like_1 = Like.objects.create(user=self.user, post=self.post_1,
                                          like='like')
        self.like_2 = Like.objects.create(user=self.user, post=self.post_2,
                                          like='dislike')
        self.like_3 = Like.objects.create(user=self.user, post=self.post_3,
                                          like='like')

    def test_ok(self):
        data = LikeListSerializer([self.like_1, self.like_2, self.like_3], many=True).data
        expected_data = [
            {
                "post": self.post_1.title,
                "user": self.user.username,
                "like": "like",
                "date": self.like_1.date.strftime('%Y-%m-%d'),
            },
            {
                "post": self.post_2.title,
                "user": self.user.username,
                "like": "dislike",
                "date": self.like_2.date.strftime('%Y-%m-%d'),
            },
            {
                "post": self.post_3.title,
                "user": self.user.username,
                "like": "like",
                "date": self.like_3.date.strftime('%Y-%m-%d'),
            },
        ]
        self.assertEqual(expected_data, data)
