from rest_framework import generics, permissions
from .models import Post
from .serializers import PostListSerializer

class FeedView(generics.ListAPIView):
    serializer_class = PostListSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        # Assuming you have a 'following' ManyToManyField in your User model
        following_users = user.following.all()
        return Post.objects.filter(author__in=following_users).order_by('-created_at')
