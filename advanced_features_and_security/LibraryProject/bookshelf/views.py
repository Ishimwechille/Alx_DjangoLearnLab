from django.shortcuts import render
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import permission_required, login_required
from .models import Article
from .models import Book
from .forms import BookForm

#my inclusions
from django.http import HttpResponse


# ✅ View all books (any logged-in user can see this)
@login_required
def list_books(request):
    books = Book.objects.all()
    return render(request, 'relationship_app/book_list.html', {'books': books})


# ✅ Create new book (requires can_add_book permission)
@login_required
@permission_required('relationship_app.can_add_book', raise_exception=True)
def add_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('book_list')
    else:
        form = BookForm()
    return render(request, 'relationship_app/book_form.html', {'form': form, 'action': 'Add'})


# ✅ Edit a book (requires can_change_book permission)
@login_required
@permission_required('relationship_app.can_change_book', raise_exception=True)
def edit_book(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('book_list')
    else:
        form = BookForm(instance=book)
    return render(request, 'relationship_app/book_form.html', {'form': form, 'action': 'Edit'})


# ✅ Delete a book (requires can_delete_book permission)
@login_required
@permission_required('relationship_app.can_delete_book', raise_exception=True)
def delete_book(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        book.delete()
        return redirect('book_list')
    return render(request, 'relationship_app/book_confirm_delete.html', {'book': book})

# Create your views here.
def index(request):
    response = "Welcome to the Book shelf 📚"
    return HttpResponse(response)


@login_required
@permission_required('relationship_app.can_view', raise_exception=True)
def article_list(request):
    articles = Article.objects.all()
    return render(request, 'relationship_app/article_list.html', {'articles': articles})

@login_required
@permission_required('relationship_app.can_create', raise_exception=True)
def create_article(request):
    if request.method == "POST":
        form = ArticleForm(request.POST)
        if form.is_valid():
            article = form.save(commit=False)
            article.author = request.user
            article.save()
            return redirect('article_list')
    else:
        form = ArticleForm()
    return render(request, 'relationship_app/create_article.html', {'form': form})

@login_required
@permission_required('relationship_app.can_edit', raise_exception=True)
def edit_article(request, pk):
    article = get_object_or_404(Article, pk=pk)
    if request.method == "POST":
        form = ArticleForm(request.POST, instance=article)
        if form.is_valid():
            form.save()
            return redirect('article_list')
    else:
        form = ArticleForm(instance=article)
    return render(request, 'relationship_app/edit_article.html', {'form': form})

@login_required
@permission_required('relationship_app.can_delete', raise_exception=True)
def delete_article(request, pk):
    article = get_object_or_404(Article, pk=pk)
    article.delete()
    return redirect('article_list')