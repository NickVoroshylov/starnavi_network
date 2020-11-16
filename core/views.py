from collections import Counter
from itertools import groupby

from django.contrib.auth.models import User
from django_filters import rest_framework as filters
from rest_framework.generics import (CreateAPIView, GenericAPIView,
                                     ListAPIView, RetrieveAPIView)
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from rest_framework_tracking import mixins

from .models import Like, Post
from .serializers import (LikeCreateSerializer, LikeListSerializer,
                          PostCreateSerializer, PostDetailSerializer,
                          PostListSerializer, UserActivitySerializer)


DEFAULT_DAY_COUNT = 30


class PostListView(ListAPIView):
    """Display list of posts"""
    queryset = Post.objects.all()
    serializer_class = PostListSerializer
    permission_classes = [IsAuthenticated]


class PostDetailView(RetrieveAPIView):
    """Display detail post"""
    queryset = Post.objects.all()
    serializer_class = PostDetailSerializer
    permission_classes = [IsAuthenticated]


class PostCreateView(mixins.LoggingMixin, CreateAPIView):
    serializer_class = PostCreateSerializer
    permission_classes = [IsAuthenticated]


class LikeCreateView(mixins.LoggingMixin, CreateAPIView):
    serializer_class = LikeCreateSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save()


class LikeListView(mixins.LoggingMixin, ListAPIView):
    """Display list of posts"""
    queryset = Like.objects.all()
    serializer_class = LikeListSerializer


class DateRangeFilterSet(filters.FilterSet):
    date_from = filters.DateFilter(field_name='date', lookup_expr='gte')
    date_to = filters.DateFilter(field_name='date', lookup_expr='lte')

    class Meta:
        model = Like
        fields = ('date_from', 'date_to')


class AnaliticView(mixins.LoggingMixin, GenericAPIView):
    queryset = Like.objects.all()
    #permission_classes = 
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = DateRangeFilterSet

    def get(self, request, format=None):
        queryset = self.get_queryset()
        filtered_queryset = self.filter_queryset(queryset)

        # Queryset needs to be ordered by date for groupby to work correctly
        ordered_queryset = filtered_queryset.order_by('date')
        likes_by_date = groupby(ordered_queryset,
                                lambda like: like.date.strftime("%Y-%m-%d"))

        analytics = []
        for date, likes in likes_by_date:
            count = Counter(like.like for like in likes)
            analytics.append(
                {
                    'date': date,
                    'total_likes': count['like'],
                    'total_dislikes': count['dislike'],

                }
            )

        return Response(analytics)


class UserActivityView(RetrieveAPIView):
    """User activity"""
    queryset = User.objects.all()
    serializer_class = UserActivitySerializer
    #permission_classes = [IsAuthenticated]
