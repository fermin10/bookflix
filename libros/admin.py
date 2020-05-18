from django.contrib.auth.admin import UserAdmin
from users.models import User, Membresia
from django.contrib import admin
from .models import Autor, Genero, Libro, Capitulo, Comentario, Editorial
from novedades.models import Novedad
from perfiles.models import Perfil


class MyUserAdmin(UserAdmin):
    model = User

    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('credit_Card', 'expired_Card')}),
    )
admin.site.register(Membresia)
admin.site.register(Novedad)
admin.site.register(Autor)
admin.site.register(Genero)
admin.site.register(Libro)
admin.site.register(Editorial)
admin.site.register(Perfil)
admin.site.register(User, MyUserAdmin)
