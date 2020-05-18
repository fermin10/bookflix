from django.urls import path
from books import views

app_name = 'books'
urlpatterns = [
    path('', views.index, name='index'),
    path('books_list/', views.libros, name='books_list'),
    path('books_list/<int:book_id>/', views.libro, name='book'),
    path('chapter/<int:chapter_id>', views.capitulo, name='chapter'),
    path('authors/', views.autores, name='authors'),
    path('authors/<int:author_id>/', views.autores, name='author'),
    path('genres/', views.generos, name='genres'),
    path('genres/<int:genre_id>/', views.genero, name='genre'),
]
