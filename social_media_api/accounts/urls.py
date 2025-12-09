from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PostViewSet, CommentViewSet, FeedView

router = DefaultRouter()
router.register('posts', PostViewSet, basename='posts')
router.register('comments', CommentViewSet, basename='comments')

urlpatterns = [
    path('', include(router.urls)),
     path('unfollow/<int:user_id>/', UserProfileView.as_view(), name='unfollow'),
    path("feed/", FeedView.as_view(), name='feed'),  # ✅ Add this here
]
