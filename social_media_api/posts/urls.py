from django.urls import path, include
from posts import views
from rest_framework import routers

post_router = routers.DefaultRouter()
post_router.register(r'posts', views.PostAPIViewSet, basename='post')
post_router.register(r'comments', views.CommentAPIViewSet, basename='comment')


urlpatterns = [
    path('', include(post_router.urls)),
    path('feed/', views.FeedView.as_view({'get':'list'})),
    path('/posts/<int:pk>/like/', include('notifications.urls')),
    path('/posts/<int:pk>/unlike/', include('notifications.urls'))
]