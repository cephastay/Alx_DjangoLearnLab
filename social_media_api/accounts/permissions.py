from rest_framework.permissions import BasePermission
from rest_framework import permissions
from rest_framework.authtoken.models import Token

class IsUser(BasePermission):

    def has_permission(self, request, view):
        if request.user.is_authenticated:
            return True
        if request.method in permissions.SAFE_METHODS:
            return True
    
    def has_object_permission(self, request, view, obj):
        if request.user == obj:
            return True
        if request.method in permissions.SAFE_METHODS:
            return True

class TokenOwner(BasePermission):

    message = 'Access Denied: You do not have the required permissions.'

    def has_permission(self, request, view):
        if request.user.is_authenticated:
            if request.user == Token.objects.get(user=view.kwargs['pk']).user: #had to write it this way because we are using a list view so it doesn't even check object permission
                return True
    
    def has_object_permission(self, request, view, obj):
        if obj.user == request.user:
            return True
    