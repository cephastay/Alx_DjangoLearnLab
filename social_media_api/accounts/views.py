from django.shortcuts import render
from rest_framework import permissions, viewsets, mixins, generics
from accounts.serializers import UserSerializer, GroupSerializer, TokenSerializer, FollowersSerializer
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group
from accounts.permissions import IsUser, TokenOwner
from rest_framework.authtoken.models import Token

# Create your views here.
User = get_user_model()
class Register(generics.CreateAPIView):
    """
    This API handles user registration for the social media API
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    model = User
    permission_classes = [permissions.AllowAny]


class Profile(generics.RetrieveUpdateDestroyAPIView):
    """
    This API view retrieves information about users
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsUser]

class UserListAPIView(generics.ListAPIView):
    """
    This API view lists all the users
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class TokenRetrieval(generics.ListAPIView):
    """
    This API outputs the token based on the user
    """
    serializer_class = TokenSerializer
    permission_classes = [TokenOwner]

    def get_object(self):
        return super().get_object()

    def get_queryset(self):
        id = self.kwargs['pk']
        return Token.objects.filter(user_id = id)
    
# class TokenDetail(generics.RetrieveAPIView):
#     """
#     For retrieving tokens
#     """
#     serializer_class = TokenSerializer
#     permission_classes = [TokenOwner]
#     # queryset = Token.objects.all()

#     def get_queryset(self):
#         return Token.objects.all().filter(user_id=self.kwargs['pk'])

class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all().order_by('name')
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]


class FollowUsers(generics.GenericAPIView):
    """
    For Updating Followers list
    """
    queryset = get_user_model().objects.all()
    serializer_class = FollowersSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsUser]




class UnFollowUsers(generics.GenericAPIView):
    pass

