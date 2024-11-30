from django.urls import path, include
import rest_framework.urls

from api.views import BookCreateView, BookListView, BookDetailView, BookUpdateView, BookDeleteView, AuthorViewSet, api_root

from rest_framework.authtoken.views import obtain_auth_token
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'authors', AuthorViewSet, basename='authors')


urlpatterns = [

    path('books/create/', BookCreateView.as_view(), name= 'create book'),
    
    path('books/', BookListView.as_view(), name='list of books'),
    path('books/<int:pk>/', BookDetailView.as_view(), name='book details' ),

    path('books/update/<int:pk>', BookUpdateView.as_view(), name='update book'),
    path('books/delete/<int:pk>', BookDeleteView.as_view(), name='delete book'),

    path('router/', include(router.urls)),
    path('', api_root, name='home'), 

    path('api-auth/', include(rest_framework.urls)), #for authenticating access to api views
    path('api-token-auth/', obtain_auth_token), #endpoint for generating tokens for users
    
]