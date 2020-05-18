from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Autor, Genero, Libro, Capitulo, Comentario, Editorial
from datetime import date, datetime


def index(request):
    """Home page of library"""

    return render(request, 'index.html')

def verificateUser(funcion):
    def verificate(req, **kwargs):
        if not req.user.is_authenticated:
            return redirect('users:login')
        else:
            #acá deje preparado el if para la falta de pago para cuando esté el atributo ya validado
            #if !(req.user.expiredPay < datetime.now)
            #    return render(req, 'restrictions/needPayment.html')
            if req.session['myProfile'] is None:                #profile = req.session.get['myProfile']
                return redirect('perfiles:seleccionarPerfil')
            else:
                return funcion(req, **kwargs)
    return verificate


@verificateUser
def libros(request):
    """Show all books"""
    bookslst = Libro.objects.order_by('fecha_creacion').reverse()
    context = {'books': bookslst}
    return render(request, 'listado_libros.html', context)

@verificateUser
def libro(request, libro_id):
    bk = Libro.objects.get(ISBN=libro_id)
    chapters = Capitulo.objects.filter(libro=bk).order_by('num')
    comments = Comentario.objects.filter(libro=bk).order_by('fecha_creacion')
    context = {'book': bk, 'chapters': chapters, 'comments': comments, 'hoy': date.today()}
    return render(request, 'libro.html', context)

@verificateUser
def capitulo(request, chap_id):
    chap = Capitulo.objects.get(id=chap_id)
    context = {'chapter': chap}
    return render(request, 'chapter.html', context)


def autores(request):
    authrs = Autor.objects.order_by('nombre')
    context = {'authors': authrs}
    return render(request, 'autores.html', context)


def generos(request):
    gnres = Genero.objects.order_by('nombre')
    context = {'genres': gnres}
    return render(request, 'generos.html', context)


def autor(request, autor_nombre):
    author = Autor.objects.get(nombre=autor_nombre)
    books = Libro.objects.filter(autor=author).order_by('titulo')
    context = {'author': author, 'books': books}
    return render(request, 'autor.html', context)


def genero(request, genero_nombre):
    gnre = Genero.objects.get(nombre=genero_nombre)
    books = Libro.objects.filter(genero=gnre).order_by('titulo')
    context = {'genre': gnre, 'books': books}
    return render(request, 'genero.html', context)

def editorial(request, editorial_nombre):
    edtr = Editorial.objects.get(nombre=editorial_nombre)
    books = Libro.objects.filter(editorial=edtr).order_by('titulo')
    context = {'edtr': edtr, 'books': books}
    return render(request, 'editorial.html', context)