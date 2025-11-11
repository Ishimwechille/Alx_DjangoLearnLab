from django.urls import path
from .views import list_books
from .views import LibraryDetailView
from .views import index
from django.contrib.auth.views import LoginView, LogoutView
from . import views

urlpatterns = [
    # Existing URLs
    path("list_books/", list_books, name="list_books"),
    path("library_detail/", LibraryDetailView.as_view(), name="library_detail"),
    path("register/", views.register, name="register"),
    path("login/", LoginView.as_view(template_name="login.html"), name="login"),
    path("logout/", LogoutView.as_view(template_name="logout.html"), name="logout"),
    path("", index, name="index"),

    # ✅ Added Role-Based Access URLs (keep these names exact)
    path("admin-view/", views.admin_view, name="admin_view"),
    path("librarian-view/", views.librarian_view, name="librarian_view"),
    path("member-view/", views.member_view, name="member_view"),
]

