from django.contrib.auth import get_user_model
from rest_framework import viewsets, permissions, status
from rest_framework.decorators import action
from rest_framework.response import Response
from .serializers import UserSerializer

User = get_user_model()


class IsSelfOrReadOnly(permissions.BasePermission):
    """
    Allow read-only for others; only allow modifications to your own user instance.
    """
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj == request.user


class UserViewSet(viewsets.ReadOnlyModelViewSet):
    """
    Viewset for user profiles with follow/unfollow actions.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    @action(detail=True, methods=["post"], permission_classes=[permissions.IsAuthenticated])
    def follow(self, request, pk=None):
        target = self.get_object()
        user = request.user

        if user == target:
            return Response({"detail": "You cannot follow yourself."}, status=status.HTTP_400_BAD_REQUEST)

        user.follow(target)
        return Response({"detail": f"You are now following {target.username}."})

    @action(detail=True, methods=["post"], permission_classes=[permissions.IsAuthenticated])
    def unfollow(self, request, pk=None):
        target = self.get_object()
        user = request.user

        if user == target:
            return Response({"detail": "You cannot unfollow yourself."}, status=status.HTTP_400_BAD_REQUEST)

        user.unfollow(target)
        return Response({"detail": f"You unfollowed {target.username}."})

    @action(detail=True, methods=["get"])
    def followers(self, request, pk=None):
        target = self.get_object()
        queryset = target.followers.all()

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = UserSerializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        return Response(UserSerializer(queryset, many=True).data)

    @action(detail=True, methods=["get"])
    def following(self, request, pk=None):
        target = self.get_object()
        queryset = target.following.all()

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = UserSerializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        return Response(UserSerializer(queryset, many=True).data)
