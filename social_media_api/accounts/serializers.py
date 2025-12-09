from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import Post, Comment
from rest_framework import serializers
from django.contrib.auth import get_user_model
from rest_framework.authtoken.models import Token




User = get_user_model()

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'bio', 'profile_picture']

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data.get('email'),
            password=validated_data['password'],
            bio=validated_data.get('bio', ''),
            profile_picture=validated_data.get('profile_picture')
        )
        Token.objects.create(user=user)
        return user

class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)

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
