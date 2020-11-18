# DRF Starnavi Social Network

This is test task for Starnavi company. The assignment consists of two parts. The first is creating an Api for a social network. The second task is to create a bot that reads parameters from a config file and simulates user actions.

## Main requirements

### Basic futures for API
* user signup
* user login
* post creation 
* post like
* post dislike
* analytics about how many likes was made by day
* user activity an endpoint which will show when user was login last time and when he mades a last
request to the service

### Basic futures for bot
Object of this bot demonstrate functionalities of the system according to defined rules. This bot
should read rules from a config file (in any format chosen by the candidate), but should have
following fields (all integers, candidate can rename as they see fit). 

* number_of_users
* max_posts_per_user
* max_likes_per_user

## Features
* All required futures
* Djoser - for JWT implementation
* Swagger - for API documentation