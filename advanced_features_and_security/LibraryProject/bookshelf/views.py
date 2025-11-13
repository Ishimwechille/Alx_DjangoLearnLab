from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, permission_required
from django.db.models import Q
from .models import Book
from .forms import BookForm, SearchForm,ExampleForm

@login_required
def book_list(request):
    form = SearchForm(request.GET or None)
    books = Book.objects.all()

    if form.is_valid():
        q = form.cleaned_data.get('q')
        if q:
            # Use ORM with parameterized queries — no raw SQL
            books = books.filter(
                Q(title__icontains=q) |
                Q(author__name__icontains=q)
            )

    context = {'books': books, 'form': form}
    return render(request, 'bookshelf/book_list.html', context)


@login_required
@permission_required('bookshelf.can_add_book', raise_exception=True)
def add_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('bookshelf:book_list')
    else:
        form = BookForm()
    return render(request, 'bookshelf/form_example.html', {'form': form, 'title': 'Add Book'})


@login_required
@permission_required('bookshelf.can_change_book', raise_exception=True)
def edit_book(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('bookshelf:book_list')
    else:
        form = BookForm(instance=book)
    return render(request, 'bookshelf/form_example.html', {'form': form, 'title': 'Edit Book'})


@login_required
@permission_required('bookshelf.can_delete_book', raise_exception=True)
def delete_book(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        book.delete()
        return redirect('bookshelf:book_list')
    return render(request, 'bookshelf/delete_confirm.html', {'book': book})
