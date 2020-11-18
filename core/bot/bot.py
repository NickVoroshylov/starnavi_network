import os
import sys
import requests
import json
import random

import django
from django.http import JsonResponse

sys.path.append('../..')
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'network.settings')
django.setup()

from django.contrib.auth.models import User
from core.models import Post


def start_bot():

    with open('./bot_conditions.json', 'r') as read_file:
        bot = json.load(read_file)

    def create_user():
        create_url = 'http://127.0.0.1:8000/api/auth/users/'
        login_url = 'http://127.0.0.1:8000/api/auth/token/login/'
        user_data = {
            "username": 'user_{}'.format(''.join(['{}'.format(random.randrange(0, 9)) for _ in range(3)])),
            "password": 'password_{}'.format(''.join(['{}'.format(random.randrange(0, 9)) for _ in range(3)]))
        }

        requests.post(create_url, data=user_data) # create user
        requests.post(login_url, data=user_data) # login to system and get token
        print(f'User {user_data["username"]} was registered with password: {user_data["password"]}')

    def post_create(user, headers):
        url = 'http://127.0.0.1:8000/api/core/post_create/'
        post_data = {
            "author": user.id,
            "title": user.username + '_test_post_{}'.format(''.join(['{}'.format(random.randrange(0, 9)) for _ in range(3)])),
            "body": user.username + ' body for post'
        }
        requests.post(url, headers=headers, data=post_data)
        print(f'Post with title: {post_data["title"]} was created by {user.username}')

    def post_like(user, headers):
        all_posts = Post.objects.all()
        random_post_id = random.choice([i.id for i in all_posts])
        like_choice = random.choice(['like', 'dislike'])
        like_url = 'http://127.0.0.1:8000/api/core/like_create/'
        like_data = {
            "user": user.id,
            "post": random_post_id,
            "like": like_choice
        }

        requests.post(like_url, headers=headers, data=like_data)
        print(f'User {user.username} {like_data["like"]} post with id {like_data["post"]}')

    for _ in range(bot['number_of_users']):
        create_user()
        active_user = User.objects.all().last()
        headers = {'Authorization': 'Token {}'.format(active_user.auth_token.key)}
        print(f'User {active_user.id} have autorization token: {active_user.auth_token.key}')
        for _ in range(bot['max_posts_per_user']):
            post_create(active_user, headers)
        for _ in range(bot['max_likes_per_user']):
            post_like(active_user, headers)
    return JsonResponse(bot, safe=True)


start_bot()
