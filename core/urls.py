from django.urls import path

from . import views


urlpatterns = [
    path('core/posts/', views.PostListView.as_view()),
    path('core/post_detail/<int:pk>/', views.PostDetailView.as_view()),
    path('core/post_create/', views.PostCreateView.as_view()),
    path('core/like_create/', views.LikeCreateView.as_view()),
    path('core/likes/', views.LikeListView.as_view()),
    path('analitic/', views.AnaliticView.as_view()),
    path('activity/<int:pk>/', views.UserActivityView.as_view()),
]
