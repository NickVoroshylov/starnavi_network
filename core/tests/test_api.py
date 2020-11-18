import json

from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.test import APITestCase

from core.models import Like, Post
from core.serializers import (LikeListSerializer, PostDetailSerializer,
                              PostListSerializer)


class PostApiTestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.token = Token.objects.create(user=self.user)
        self.post_1 = Post.objects.create(author=self.user, title='Test post 1',
                                          body='Test body')
        self.post_2 = Post.objects.create(author=self.user, title='Test post 2',
                                          body='Test body 2')

    def test_get(self):
        url = reverse('post_list')
        response = self.client.get(url)
        serializer_data = PostListSerializer([self.post_1, self.post_2], many=True).data
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(serializer_data, response.data)

    def test_create(self):
        self.assertEqual(2, Post.objects.all().count())
        url = reverse('post_create')
        data = {
            "title": self.post_1.title,
            "body": self.post_1.body,
            "author": self.user.id
        }
        json_data = json.dumps(data)
        response = self.client.post(url, HTTP_AUTHORIZATION='Token {}'.format(self.token),
                                    data=json_data, content_type='application/json')
        self.assertEqual(status.HTTP_201_CREATED, response.status_code)
        self.assertEqual(3, Post.objects.all().count())

    def test_detail(self):
        url = reverse('post_detail', args=(self.post_1.id,))
        response = self.client.get(url, HTTP_AUTHORIZATION='Token {}'.format(self.token))
        serializer_data = PostDetailSerializer(self.post_1).data
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(serializer_data, response.data)


class LikeApiTestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.token = Token.objects.create(user=self.user)
        self.post_1 = Post.objects.create(author=self.user, title='Test post 1',
                                          body='Test body')
        self.post_2 = Post.objects.create(author=self.user, title='Test post 2',
                                          body='Test body 2')
        self.post_3 = Post.objects.create(author=self.user, title='Test post 3',
                                          body='Test body 3')
        self.like_1 = Like.objects.create(user=self.user, post=self.post_1, 
                                          like='like')
        self.like_2 = Like.objects.create(user=self.user, post=self.post_2, 
                                          like='like')

    def like_get(self):
        url = reverse('like_list')
        response = self.client.get(url)
        serializer_data = LikeListSerializer([self.like_1, self.like_2], many=True).data
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(serializer_data, response.data)

    def like_create(self):
        self.assertEqual(2, Like.objects.all().count())
        self.assertEqual(0, Like.objects.filter(like='dislike').count())
        url = reverse('like_create')
        data = {
            "user": self.user.id,
            "post": self.post_3.id,
            "like": "dislike"
        }
        json_data = json.dumps(data)
        response = self.client.post(url, HTTP_AUTHORIZATION='Token {}'.format(self.token),
                                    data=json_data, content_type='application/json')
        self.assertEqual(status.HTTP_201_CREATED, response.status_code)
        self.assertEqual(3, Like.objects.all().count())
        self.assertEqual(1, Like.objects.filter(like='dislike').count())
