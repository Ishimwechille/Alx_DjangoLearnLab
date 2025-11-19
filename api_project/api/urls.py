# api/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BookList, 
from .views import BookViewSet.
from rest_framework.authtoken.views import obtain_auth_token


router = DefaultRouter()
router.register(r'books_all', BookViewSet, basename='book_all')

urlpatterns = [
    path('books/', BookList.as_view(), name='book-list'),  # Optional: keep if you want a separate list view
    path('', include(router.urls)),  # Auto-generates all CRUD routes
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),


]




urlpatterns = [
    path('books/', BookList.as_view(), name='book-list'),
]
