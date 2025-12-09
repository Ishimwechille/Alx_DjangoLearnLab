# accounts/models.py
from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    bio = models.TextField(blank=True, null=True)
    profile_picture = models.ImageField(upload_to='profile_pics/', blank=True, null=True)
    followers = models.ManyToManyField('self', symmetrical=False, related_name='following', blank=True)

    def __str__(self):
        return self.username

class User(AbstractUser):
    """
    Custom user model that supports following other users.
    'following' is the set of users this user follows.
    'followers' is the reverse relation (users who follow this user).
    """
    following = models.ManyToManyField(
        "self",
        symmetrical=False,
        related_name="followers",
        blank=True,
    )

    def follow(self, user):
        """Follow the provided user (no-op if already following)."""
        if user and user != self:
            self.following.add(user)

    def unfollow(self, user):
        """Unfollow the provided user (no-op if not following)."""
        if user and user != self:
            self.following.remove(user)

    def is_following(self, user):
        return self.following.filter(pk=user.pk).exists()
