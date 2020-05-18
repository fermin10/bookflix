from django.db import models
from users.models import User


class Perfil(models.Model):
    nombre = models.CharField(max_length=10)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    class Meta:
        verbose_name_plural = "perfiles"
    def __str__(self):
        return self.nombre