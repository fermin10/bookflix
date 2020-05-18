from django.contrib.auth.models import AbstractUser
from django.db import models
from creditcards.models import CardNumberField, CardExpiryField, SecurityCodeField


class Membresia(models.Model):
    nombre = models.CharField(max_length=10)
    limitePerfiles = models.PositiveSmallIntegerField()
    limiteSesionesActivas = models.PositiveSmallIntegerField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.nombre

class User(AbstractUser):
    credit_Card = CardNumberField('Número de tarjeta', null=True, unique=True)
    expired_Card = CardExpiryField('Fecha de vencimiento', null=True)
    secCode_Card = SecurityCodeField('Código de seguridad', null=True)
    tipo_tarjeta = models.CharField('Tipo de tarjeta', null=True, max_length=60)
    titular = models.CharField('Nombre del titular de la tarjeta', null=True, max_length=60)
    subscription = models.ForeignKey(Membresia, on_delete=models.CASCADE, null=True, blank=True)
    dni = models.IntegerField('DNI del titular de la tarjeta', null=True)


    def __str__(self):
        return self.username