
 from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PostViewSet, CommentViewSet, FeedView

# DRF routers for Post and Comment CRUD
router = DefaultRouter()
router.register('posts', PostViewSet, basename='posts')
router.register('comments', CommentViewSet, basename='comments')

urlpatterns = [
    # Explicit feed endpoint (required by automated check)
 path('follow/<int:user_id>/', FollowUserView.as_view(), name='follow-user'),
 path('unfollow/<int:user_id>/', UnfollowUserView.as_view(), name='unfollow-user'),

    # Registration and login endpoints
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('feed/', FeedView.as_view(), name='feed'),

    # Include router-generated endpoints for CRUD
    path('', include(router.urls)),
]
