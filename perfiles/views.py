from django.shortcuts import render, redirect
from .forms import crearPerfil
from .models import Perfil
from novedades.models import Novedad
from datetime import date
from time import strptime
from libros.models import Libro

def nuevoPerfil(request):
    usuario = request.user
    countProfiles = Perfil.objects.filter(usuario=usuario).count()
    if (countProfiles == usuario.subscription.limitePerfiles):
        context= {'usuario':usuario}
        return render(request, 'error.html', context)
    else:
        if request.method != 'POST':
            # se muestra un form en blanco para registrarlo
            form = crearPerfil()
        else:
            # se procesa un form completado
            form = crearPerfil(request.POST)
            if form.is_valid():
                if (not usuario.subscription is None):
                    new_profile = form.save(commit=False)
                    new_profile.usuario = usuario
                    new_profile.save()
                    return seleccionarPerfil(request)


    context = {'form': form}
    return render(request, 'nuevoPerfil.html', context)




def seleccionarPerfil(request):


    request.session['myProfile'] = None

    if request.user.is_staff:
        profiles = Perfil.objects.get(usuario=request.user)
        return viewIndex(request, profiles.id)
    else:
        profiles = Perfil.objects.all()
        profiles = profiles.filter(usuario=request.user)
        context = {'perfiles': profiles}
        return render(request, 'seleccionarPerfil.html', context)


def viewIndex(request, perfil_id):
    profile = Perfil.objects.get(id=perfil_id)
    request.session['myProfile'] = perfil_id
    #request.session.set_expiry(0) ¿como borro el atributo (del request.session['myProfile'])
    novs = Novedad.objects.order_by('fechaLanzamiento')
    novss = filter(lambda x : x.fechaLanzamiento <= date.today(), novs )
    bookslst = Libro.objects.order_by('titulo')
    context = {'perfil': profile, 'novedades': novss, 'libros': bookslst}
    return render(request, 'index.html', context)

def verPerfil(request):
    try:
        profile = Perfil.objects.get(id=request.session['myProfile'])
        context = {'perfil': profile}
        return render(request, 'verPerfil.html', context)
    except:
        return seleccionarPerfil(request)

