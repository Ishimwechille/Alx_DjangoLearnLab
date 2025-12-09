from .views import FeedView

urlpatterns = [
    path('register/', RegisterUserView.as_view(), name='register'),
    path('login/', LoginUserView.as_view(), name='login'),
    path('profile/', UserProfileView.as_view(), name='profile'),
    path('follow/<int:user_id>/', UserProfileView.as_view(), name='follow'),
    path('unfollow/<int:user_id>/', UserProfileView.as_view(), name='unfollow'),
    path('feed/', FeedView.as_view(), name='feed'),  # ✅ New route
]
