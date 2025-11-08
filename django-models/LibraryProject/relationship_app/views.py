from django.shortcuts import render
from .models import Book, Library
from django.views.generic import DetailView

# Function-based view to list all books
def list_books(request):
    books = Book.objects.all()
    return render(request, 'list_books.html', {'books': books})

