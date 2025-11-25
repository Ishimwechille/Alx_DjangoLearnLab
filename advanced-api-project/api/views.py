# api/views.py
from rest_framework import generics, permissions
from .models import Book
from .serializers import BookSerializer


# ListView – Public access
class ListView(generics.ListAPIView):
    """
    Returns a list of all books.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.AllowAny]


# DetailView – Public access
class DetailView(generics.RetrieveAPIView):
    """
    Returns a single book using its ID.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.AllowAny]


# CreateView – Requires authentication
class CreateView(generics.CreateAPIView):
    """
    Creates a new book. Only authenticated users can create books.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]


# UpdateView – Requires authentication
class UpdateView(generics.UpdateAPIView):
    """
    Updates an existing book. Only authenticated users can update books.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]


# DeleteView – Requires authentication
class DeleteView(generics.DestroyAPIView):
    """
    Deletes a book. Only authenticated users can delete books.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]
