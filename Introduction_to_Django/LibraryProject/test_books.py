import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'LibraryProject.settings')
django.setup()

from bookshelf.models import Book

# Create
book = Book.objects.create(title="1984", author="George Orwell", publication_year=1949)
print(book)

# Retrieve
books = Book.objects.all()
for b in books:
    print(b.title, b.author, b.publication_year)

# Update
book.title = "Nineteen Eighty-Four"
book.save()
print(book)

# Delete
book.delete()
print(Book.objects.all())
