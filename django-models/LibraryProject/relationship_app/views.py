from django.shortcuts import render

# Create your views here.
from .models import Library
from .models import Author, Librarian, Book, Library
from django.views.generic import ListView
from django.views.generic import DetailView
from django.views.generic.detail import DetailView
from django.http import HttpResponse

from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic import CreateView

from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm

def index(request):
    # """Renders the index page of the relationship app."""
    # return render(request, 'index.html')
    return HttpResponse("This is the index page of the relationship app.")

def list_books(request):
      """Retrieves all books and renders a template displaying the list."""
      books = Book.objects.all()  # Fetch all book instances from the database
      context = {'book_list': books}  # Create a context dictionary with book list
      return render(request, 'relationship_app/list_books.html', context)

# Create a class-based view in relationship_app/views.py that displays details for a specific library, listing all books available in that library.
# Utilize Django’s ListView or DetailView to structure this class-based view.
class LibraryDetailView(DetailView):
    """A class-based view for displaying details of a specific library."""
    model = Library
    template_name = 'relationship_app/library_detail.html'

    def get_context_data(self, **kwargs):
        """Injects additional context data specific to the library."""
        context = super().get_context_data(**kwargs)  # Get default context data
        library = self.get_object()  # Retrieve the current library instance
        context['books'] = library.books.all()  # List all books in the library
        return context

class LibraryListView(ListView):
    """A class-based view for displaying a list of libraries."""
    model = Library
    template_name = 'relationship_app/library_detail.html'

    def get_context_data(self, **kwargs):
        """Injects additional context data specific to the library."""
        context = super().get_context_data(**kwargs)  # Get default context data
        context['libraries'] = Library.objects.all()  # List all libraries
        return context  

# Note: Ensure that the template files 'books/book_list.html', 'books/book_detail.html', and 'libraries/library_detail.html' exist in your templates directory.
# This code defines views for listing books and displaying details of a specific book and library in a Django application.

# Ensure that the necessary models (Book, Library) are defined in relationship_app/models.py.

# Create a user registration view using Django's built-in UserCreationForm.
# This view will allow users to sign up for an account.
class register(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/register.html'


# Set Up Role-Based Views
# Create three separate views to manage content access based on user roles:

# Views to Implement:

# An ‘Admin’ view that only users with the ‘Admin’ role can access, the name of the file should be admin_view
# A ‘Librarian’ view accessible only to users identified as ‘Librarians’. The file should be named librarian_view
# A ‘Member’ view for users with the ‘Member’ role, the name of the file should be member_view
# Access Control:

# Utilize the @user_passes_test decorator to check the user’s role before granting access to each view.

from django.contrib.auth.decorators import user_passes_test

def is_admin(user):
    return user.userprofile.role == 'Admin'

def is_librarian(user):
    return user.userprofile.role == 'Librarian'

def is_member(user):
    return user.userprofile.role == 'Member'

@user_passes_test(is_admin)
def admin_view(request):
    """View accessible only to Admin users."""
    return render(request, 'relationship_app/templates/admin_view.html') 

@user_passes_test(is_librarian)
def librarian_view(request):
    """View accessible only to Librarian users."""
    return render(request, 'relationship_app/templates/librarian_view.html')

@user_passes_test(is_member)
def member_view(request):
    """View accessible only to Member users."""
    return render(request, 'relationship_app/templates/member_view.html')

# Ensure that the templates 'admin_view.html', 'librarian_view.html', and 'member_view.html' exist in your templates directory.
# This code defines views for user registration and role-based access control in a Django application.


# Step 1: Extend the Book Model with Custom Permissions
# Add custom permissions to the Book model to specify who can add, edit, or delete the entries.

# Model Changes Required:
# Inside the Book model, define a nested Meta class.
# Within this Meta class, specify a permissions tuple that includes permissions like can_add_book, can_change_book, and can_delete_book.
# Step 2: Update Views to Enforce Permissions
# Adjust your views to check if a user has the necessary permissions before allowing them to perform create, update, or delete operations.

# Views to Modify:
# Use Django’s permission_required decorator to secure views that add, edit, or delete books.
# For each view, apply the corresponding permission.

from django.contrib.auth.decorators import permission_required

@permission_required('relationship_app.can_add_book')
def add_book(request):
    # View logic for adding a book
    pass

@permission_required('relationship_app.can_change_book')
def edit_book(request, book_id):
    # View logic for editing a book
    pass

@permission_required('relationship_app.can_delete_book')
def delete_book(request, book_id):
    # View logic for deleting a book
    pass