from django.shortcuts import render

from books.models import Book, Genre


def books_list(request):
    books = Book.objects.all()
    return render(request, 'books/books_list.html', {'books': books})
def books_detail(request, slug):
    info = Book.objects.all(genre__slug=slug)
    return render(request, 'books/books_detail.html', {'info': info})
def genre_view(request):
    genres = Genre.objects.all()
    return render(request, 'books/main_page.html', {'genres': genres})
