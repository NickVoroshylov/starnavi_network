from django.urls import path

from . import views


urlpatterns = [
    path('core/posts/', views.PostListView.as_view(), name='post_list'),
    path('core/post_detail/<int:pk>/', views.PostDetailView.as_view(), name='post_detail'),
    path('core/post_create/', views.PostCreateView.as_view(), name='post_create'),
    path('core/like_create/', views.LikeCreateView.as_view(), name='like_create'),
    path('core/likes/', views.LikeListView.as_view(), name='like_list'),
    path('analitic/', views.AnaliticView.as_view(), name='user_analitic'),
    path('activity/<int:pk>/', views.UserActivityView.as_view(), name='users_activity'),
]
