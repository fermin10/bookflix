from django.db import models
from users.models import User


class Genero(models.Model):
    nombre = models.CharField(max_length=50)


    def __str__(self):
        return self.nombre


class Autor(models.Model):
    nombre = models.CharField(primary_key=True,max_length=50)

    def __str__(self):
        return self.nombre

class Editorial(models.Model):

    nombre = models.CharField(primary_key=True, max_length=50)

    def __str__(self):
        return self.nombre


class Libro(models.Model):
    ISBN = models.IntegerField(primary_key=True)
    titulo = models.CharField(max_length=50)
    autor = models.ForeignKey(Autor, on_delete=models.CASCADE)
    sinopsis = models.TextField()
    editorial = models.ForeignKey(Editorial, on_delete=models.CASCADE, null=True)
    genero = models.ForeignKey(Genero, on_delete=models.CASCADE)
    calificacion = models.FloatField()
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titulo


class Capitulo(models.Model):
    libro = models.ForeignKey(Libro, on_delete=models.CASCADE)
    titulo = models.CharField(max_length=30)
    num = models.PositiveIntegerField()
    texto = models.FileField()
    paginas = models.IntegerField(blank=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.titulo


class Comentario(models.Model):
    libro = models.ForeignKey(Libro, on_delete=models.CASCADE)
    texto = models.TextField()
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    spoiler = models.BooleanField()

    def __str__(self):
        if len(self.texto) > 50:
            frase = self.texto[:50] + "..."
        else:
            frase = self.texto
        return frase

