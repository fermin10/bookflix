from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import UCFWithExtends, configurarCuenta

def register(request):
    """Register a new user"""
    if request.method != 'POST':
        # se muestra un form en blanco para registrarlo
        form = UCFWithExtends()
    else:
        # se procesa un form completado
        form = UCFWithExtends(data=request.POST)
        if form.is_valid():
            new_user = form.save()  # guardo un objeto 'user' en la variablo new_user que dsp se pasa como parametro a login()
            # logear al usuario y redirigirlo a la pagina de inicio
            login(request, new_user)  # funcion propia de django, fabulosa
            return redirect('perfiles:seleccionarPerfil')
    # se muestra un form vacio o invalido
    context = {'form': form}
    return render(request, 'registration/register.html', context)

def configurar(request):
    form = configurarCuenta(instance=request.user)
    if request.method != 'POST':
        # se muestra un form en blanco para registrarlo
        form = configurarCuenta(instance=request.user)
    else:
        form = configurarCuenta(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('users:configurar')

    context = {'form': form}
    return render(request, 'configurarCuenta.html', context)