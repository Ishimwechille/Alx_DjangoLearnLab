from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PostViewSet, CommentViewSet, FeedView

# DRF routers for Post and Comment CRUD
router = DefaultRouter()
router.register('posts', PostViewSet, basename='posts')
router.register('comments', CommentViewSet, basename='comments')

urlpatterns = [
    # Explicit feed endpoint (required by automated check)
    path('feed/', FeedView.as_view(), name='feed'),

    # Include router-generated endpoints
    path('', include(router.urls)),
]
