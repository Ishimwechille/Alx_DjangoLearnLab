from django.shortcuts import render
from .models import Book
from .models import Library

# Function-based view to list all books
def list_books(request):
    books = Book.objects.all()  # ✅ Fetch all books
    return render(request, 'relationship_app/list_books.html', {'books': books})  # ✅ Render the correct template
