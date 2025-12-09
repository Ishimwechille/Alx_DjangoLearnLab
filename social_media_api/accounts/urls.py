
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PostViewSet, CommentViewSet, FeedView

# DRF router for posts and comments
router = DefaultRouter()
router.register('posts', PostViewSet, basename='posts')
router.register('comments', CommentViewSet, basename='comments')

urlpatterns = [
    path('', include(router.urls)),
    path('feed/', FeedView.as_view(), name='feed'),  # ✅ This is the required feed route
    path('unfollow/<int:user_id>/', UserProfileView.as_view(), name='unfollow'),
]
