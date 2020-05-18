from django.urls import path
from novedades import views

app_name = 'novedades'
urlpatterns = [

    path('', views.index, name='index'),
    path('novedad/<int:novedad_id>', views.novedad, name='novedad'),
    path('novedades/', views.novedades, name='listado_novedades')

]
