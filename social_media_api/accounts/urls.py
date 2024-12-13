from django.urls import path, include
from accounts.views import Register, TokenRetrieval, Profile, GroupViewSet, UserListAPIView, FollowUsers, UnFollowUsers
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'groups', GroupViewSet)
# router.register(r'follow/', FollowUsers)

urlpatterns = [

    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),

    path('register/', Register.as_view(), name='register'),

    path('profile/<int:pk>/', Profile.as_view(), name='customuser-detail'),
    path('profile/', UserListAPIView.as_view(), name='users'),
    path('profile/<int:pk>/token/', TokenRetrieval.as_view(), name='token'),

    # path('token/<int:pk>/', TokenDetail.as_view(), name='token-detail'),

    path('login/', include('rest_framework.urls', namespace='rest_framework')),
    path('', include(router.urls)),

    # path('follow/', FollowUsers.as_view({'get':'list'}), name='follow-user'),
    path('follow/<int:user_id>/', FollowUsers.as_view() ),
    path('unfollow/<int:user_id>/', UnFollowUsers.as_view())
]