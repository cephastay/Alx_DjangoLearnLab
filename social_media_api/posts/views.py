from django.shortcuts import render
from rest_framework import viewsets, generics, permissions
from posts.serializers import PostSerializer, CommentSerializer
from posts.models import Post, Comment
from posts.permissions import IsOwnerOrReadOnly

from django_filters import rest_framework as r_filters
from rest_framework import filters
from rest_framework.pagination import PageNumberPagination

# Create your views here.

class PostAPIViewSet(viewsets.ModelViewSet):
    serializer_class = PostSerializer
    queryset = Post.objects.all().prefetch_related('post_comments')

    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

    filter_backends = [filters.SearchFilter, filters.OrderingFilter, r_filters.DjangoFilterBackend]
    search_fields = ['author__username', 'title', 'content']
    ordering_fields = ['title']
    filterset_fields = ['created_at']
    # pagination_class = [PageNumberPagination]
    # page_size = 5

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

class CommentAPIViewSet(viewsets.ModelViewSet):

    serializer_class  = CommentSerializer
    queryset = Comment.objects.all()

    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user) 

#! Ignore
from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404
class FeedView(viewsets.ModelViewSet):
    following = get_object_or_404(get_user_model(), pk=1).follows
    following_users = following.all()
    queryset = Post.objects.filter(author__in=following_users).order_by('-created_at')
