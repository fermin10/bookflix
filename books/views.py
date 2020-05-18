from django.shortcuts import render, redirect
from .models import Autor, Genero, Libro, Capitulo, Comentario


def index(request):
    """Home page of library"""
    return render(request, 'books/index.html')


def libros(request):
    """Show all books"""
    bookslst = Libro.objects.order_by('titulo')
    context = {'books': bookslst}
    return render(request, 'books/books_list.html', context)


def libro(request, book_id):
    bk = Libro.objects.get(ISBN=book_id)
    chapters = Capitulo.objects.filter(book=bk).order_by('num')
    comments = Comentario.objects.filter(book=bk).order_by('fecha_creacion')
    context = {'book': bk, 'chapters': chapters, 'comments': comments}
    return render(request, 'books/book.html', context)


def capitulo(request, chap_id):
    chap = Capitulo.objects.get(id=chap_id)
    context = {'chapter': chap}
    return render(request, 'books/chapter.html', context)


def autores(request):
    authrs = Autor.objects.order_by('nombre')
    context = {'authors': authrs}
    return render(request, 'books/authors.html', context)


def generos(request):
    gnres = Genero.objects.order_by('nombre')
    context = {'genres': gnres}
    return render(request, 'books/genres.html', context)


def autor(request, author_id):
    author = Autor.objects.get(id=author_id)
    books = Libro.objects.filter(author=author).order_by('titulo')
    context = {'author': author, 'books': books}
    return render(request, 'books/author.html', context)


def genero(request, genre_id):
    gnre = Genero.objects.get(id=genre_id)
    books = Libro.objects.filter(genre=gnre).order_by('titulo')
    context = {'genre': gnre, 'books': books}
    return render(request, 'books/genre.html', context)