from django.urls import path
from libros import views

app_name = 'libros'
urlpatterns = [
    path('index', views.index, name='index'),
    path('listado_libros/', views.libros, name='listado_libros'),
    path('listado_libros/<int:libro_id>/', views.libro, name='libro'),
    path('chapter/<int:chapter_id>', views.capitulo, name='chapter'),
    path('autores/', views.autores, name='autores'),
    path('autor/<str:autor_nombre>/', views.autor, name='autor'),
    path('genres/', views.generos, name='genres'),
    path('genero/<str:genero_nombre>/', views.genero, name='genero'),
    path('editorial/<str:editorial_nombre>/', views.editorial, name='editorial')

]
