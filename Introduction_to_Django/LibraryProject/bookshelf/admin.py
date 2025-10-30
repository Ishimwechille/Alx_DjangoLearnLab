from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Book

# Customizing the admin interface
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publication_year')  # Columns to show in admin list
    list_filter = ('publication_year', 'author')  # Add filters on the right sidebar
    search_fields = ('title', 'author')  # Enable search by title or author

# Register model and its custom admin configuration
admin.site.register(Book, BookAdmin)

