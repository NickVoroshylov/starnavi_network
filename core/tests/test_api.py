from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework.test import APITestCase


class PostApiTestCase(APITestCase):
    def test_get(self):
        url = reverse('posts/')
        print(url)
        response = self.client.get(url)
        print(response)
