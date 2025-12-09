from rest_framework import generics, permissions,
from .models import Post,
from .serializers import PostListSerializer,
from rest_framework import viewsets, permissions,
from rest_framework.permissions import IsAuthenticated,
from .models import Post, Comment,
from .serializers import PostListSerializer, PostDetailSerializer, CommentSerializer
from rest_framework.routers import DefaultRouter,
from django.urls import path, include
from .views import PostViewSet, CommentViewSet, FeedView,
from .views import FeedView,



# DRF router for posts and comments
router = DefaultRouter()
router.register('posts', PostViewSet, basename='posts')
router.register('comments', CommentViewSet, basename='comments')

urlpatterns = [
    path('', include(router.urls)),           # posts/ and comments/ endpoints
    path("feed/", FeedView.as_view(), name="feed"),  # ✅ feed endpoint
]

# Custom permission to allow users to edit/delete only their own objects
class IsOwnerOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        # Read-only permissions are allowed for any request
        if request.method in permissions.SAFE_METHODS:
            return True
        # Write permissions only if the user is the owner
        return obj.author == request.user

# -------------------------
# Post ViewSet
# -------------------------
class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()  # Required by the check
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]

    def get_serializer_class(self):
        if self.action in ['list']:
            return PostListSerializer
        return PostDetailSerializer

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

# -------------------------
# Comment ViewSet
# -------------------------
class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()  # Required by the check
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

class FeedView(generics.ListAPIView):
    serializer_class = PostListSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        # Assuming you have a 'following' ManyToManyField in your User model
        following_users = user.following.all()
        return Post.objects.filter(author__in=following_users).order_by('-created_at')
