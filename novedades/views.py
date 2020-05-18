from django.shortcuts import render
from .models import Novedad
from datetime import date
from time import strptime
from libros.models import Libro
from libros.views import verificateUser
# Create your views here.


def index(request):
    novs = Novedad.objects.order_by('fechaLanzamiento')
    novss = filter(lambda x : x.fechaLanzamiento <= date.today(), novs )
    bookslsts = Libro.objects.order_by('fecha_creacion').reverse()[0:7]
    bookslst = filter(lambda x : x.fecha_lanzamiento <= date.today(), bookslsts )
    context = {'novedades': novss, 'libros': bookslst}
    return render(request, 'index.html', context)

def novedades(request):
    novs = Novedad.objects.order_by('fechaLanzamiento')
    novss = filter(lambda x : x.fechaLanzamiento <= date.today(), novs )
    context = {'novedades': novss}
    return render(request, 'listado_novedades.html', context)

def novedad(request, novedad_id):
    nov = Novedad.objects.get(id=novedad_id)
    lib = nov.libro
    context = {'novedad' : nov, 'libro': lib}
    return render(request, 'novedad.html', context)