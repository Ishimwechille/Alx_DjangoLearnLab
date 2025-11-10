
from django.urls import path
from . import views
from .views import is_librarian, list_books, LibraryDetailView, LibraryListView
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path("", views.index, name="index"),
    path("book_list/", list_books, name="book_list"),
    path("libraries/", LibraryListView.as_view(), name="library_detail"),
    path('login/', LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='registration/logout.html'), name='logout'),
    path('register/', views.register.as_view(), name='register'),
    path("librarian_view/", views.librarian_view, name="librarian_view", kwargs={'permission_required': 'relationship_app.can_view_librarian'}),
    path("member_view/", views.member_view, name="member_view", kwargs={'permission_required': 'relationship_app.can_view_member'}),
    # path("admin_view/", views.admin_view, name="admin_view", kwargs={'permission_required': 'relationship_app.can_view_admin'}, role_required='Admin'),
    path("delete_book/", views.delete_book, name="delete_book", kwargs={'permission_required': 'relationship_app.can_delete_book'}),
    path("add_book/", views.add_book, name="add_book", kwargs={'permission_required': 'relationship_app.can_add_book'}),
    path("edit_book/", views.edit_book, name="edit_book", kwargs={'permission_required': 'relationship_app.can_change_book'}),
]


# Note: Ensure that the views and templates referenced in the URLs exist and are correctly implemented.
# The urlpatterns list routes URLs to views. For more information please see: https://docs.djangoproject.com/en/stable/topics/http/urls/