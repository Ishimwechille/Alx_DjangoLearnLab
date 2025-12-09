from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import Post, Comment

User = get_user_model()


# --------------------------------------
# User Serializer (for followers feature)
# --------------------------------------
class UserSerializer(serializers.ModelSerializer):
    followers_count = serializers.IntegerField(source="followers.count", read_only=True)
    following_count = serializers.IntegerField(source="following.count", read_only=True)

    class Meta:
        model = User
        fields = [
            "id",
            "username",
            "email",
            "first_name",
            "last_name",
            "followers_count",
            "following_count",
        ]
        read_only_fields = ["id", "followers_count", "following_count"]


# -------------------------
# Comment Serializer
# -------------------------
class CommentSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField(read_only=True)
    author_id = serializers.PrimaryKeyRelatedField(
        source="author",
        queryset=User.objects.all(),
        write_only=True,
        required=False
    )

    class Meta:
        model = Comment
        fields = [
            "id",
            "post",
            "content",
            "author",
            "author_id",
            "created_at",
            "updated_at"
        ]
        read_only_fields = ["id", "author", "created_at", "updated_at"]


# -------------------------
# Post List Serializer
# -------------------------
class PostListSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField(read_only=True)
    comments_count = serializers.IntegerField(source="comments.count", read_only=True)

    class Meta:
        model = Post
        fields = [
            "id",
            "title",
            "author",
            "comments_count",
            "created_at",
            "updated_at"
        ]


# -------------------------
# Post Detail Serializer
# -------------------------
class PostDetailSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField(read_only=True)
    comments = CommentSerializer(many=True, read_only=True)

    class Meta:
        model = Post
        fields = [
            "id",
            "title",
            "content",
            "author",
            "comments",
            "created_at",
            "updated_at",
        ]
        read_only_fields = ["author", "created_at", "updated_at"]
