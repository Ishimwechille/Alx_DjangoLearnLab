from rest_framework.routers import DefaultRouter
from django.urls import include, path
from .views import UserViewSet, RegisterView, LoginView

# DRF router for UserViewSet (read, follow, unfollow, followers, following)
router = DefaultRouter()
router.register(r"accounts", UserViewSet, basename="user")

urlpatterns = [
    # Router URLs for UserViewSet
    path("", include(router.urls)),

    # Manual URLs for registration and login
    path("register/", RegisterView.as_view(), name="register"),
    path("login/", LoginView.as_view(), name="login"),
]
