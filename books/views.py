from django.shortcuts import render
from .models import Book

def book_list(request):
    query = request.GET.get('q')
    books = Book.objects.all()
    if query:
        books = books.filter(title__icontains=query)
    return render(request, 'books/book_list.html', {'books': books})
