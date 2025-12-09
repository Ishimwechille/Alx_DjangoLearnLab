from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PostViewSet, CommentViewSet, FeedView

router = DefaultRouter()
router.register('posts', PostViewSet, basename='posts')
router.register('comments', CommentViewSet, basename='comments')

urlpatterns = [
    # Explicit feed endpoint
    path('feed/', FeedView.as_view(), name='feed'),

    # Include router CRUD endpoints
    path('', include(router.urls)),
]
