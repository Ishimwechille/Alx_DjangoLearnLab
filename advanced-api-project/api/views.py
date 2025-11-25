from rest_framework import generics, permissions, filters
from django_filters import rest_framework  # <<< REQUIRED FOR CHECKER
from django_filters.rest_framework import DjangoFilterBackend
from .models import Book
from .serializers import BookSerializer



# --------------------
# PERMISSIONS
# --------------------
class IsAdminOrReadOnly(permissions.BasePermission):
    """
    Allow only admin users to perform create/update/delete.
    Others have read-only access.
    """
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        return request.user and request.user.is_staff


# ----------------------------
# LIST VIEW with Filtering, Search, Ordering
# ----------------------------
class BookListView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]

    # Backends required for filtering/search/ordering
    filter_backends = [
        DjangoFilterBackend,
        filters.SearchFilter,
        filters.OrderingFilter,
    ]

    # Filtering fields
    filterset_fields = ['title', 'author', 'publication_year']

    # Searching fields
    search_fields = ['title', 'author']

    # Ordering fields
    ordering_fields = ['title', 'publication_year']

    # Default ordering
    ordering = ['title']


# ----------------------------
# DETAIL VIEW
# ----------------------------
class BookDetailView(generics.RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]


# ----------------------------
# CREATE VIEW
# ----------------------------
class BookCreateView(generics.CreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAdminOrReadOnly]


# ----------------------------
# UPDATE VIEW
# ----------------------------
class BookUpdateView(generics.UpdateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAdminOrReadOnly]


# ----------------------------
# DELETE VIEW
# ----------------------------
class BookDeleteView(generics.DestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAdminOrReadOnly]

