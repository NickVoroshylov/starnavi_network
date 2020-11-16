from django.urls import path

from . import views


urlpatterns = [
    path('core/', views.PostListView.as_view()),
    path('core/<int:pk>/', views.PostDetailView.as_view()),
    path('core/create/', views.PostCreateView.as_view()),
    path('activity/<int:pk>/', views.UserActivityView.as_view()),
    path('core/like/', views.LikeCreateView.as_view()),
    path('core/likes/', views.LikeListView.as_view()),
    path('analitic/', views.AnaliticView.as_view())
]
