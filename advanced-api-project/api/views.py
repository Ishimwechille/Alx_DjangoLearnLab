from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated, AllowAny


# Create your views here.
/books/                 → List all books
/books/<int:pk>/        → Get a single book
/books/create/          → Create
/books/<int:pk>/update/ → Update
/books/<int:pk>/delete/ → Delete


