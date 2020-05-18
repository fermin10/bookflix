from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User, Membresia
import datetime

# Extendemos del original
class UCFWithExtends(UserCreationForm):
    # Ahora el campo username es de tipo email y cambiamos su texto

    username =forms.EmailField(max_length=50, label='', widget=forms.TextInput(attrs={'style':'margin-left:100px', 'size':'50px','placeholder':'Dirección de correo electrónico'}))
    first_name = forms.CharField(max_length=30, label="", widget=forms.TextInput(attrs={'style':'margin-left:100px', 'size':'50px','placeholder': 'Nombre'}))
    last_name = forms.CharField(max_length=30, label="", widget=forms.TextInput(attrs={'style':'margin-left:100px', 'size':'50px','placeholder': 'Apellido'}))
    password1 = forms.CharField(label="", widget=forms.PasswordInput(attrs={'style':'margin-left:100px', 'size':'50px','placeholder': 'Contraseña'}))
    password2 = forms.CharField(label="", widget=forms.PasswordInput(attrs={'style':'margin-left:100px', 'size':'50px','placeholder': 'Confirmar contraseña'}))
    subscription = forms.ModelChoiceField(queryset=Membresia.objects.all(), label="Subscripción")
    titular = forms.CharField(label='', max_length=60, widget=forms.TextInput(attrs={'style':'margin-left:100px', 'size':'50px','placeholder': 'Nombre del titular de la tarjeta'}))
    dni = forms.CharField(label="", widget=forms.TextInput(attrs={'style':'margin-left:100px', 'size':'50px','placeholder': 'DNI del titular de la tarjeta'}))
    tipo_tarjeta = forms.ChoiceField(choices=[('Crédito', 'Crédito')]+[('Débito', 'Débito')], label='Tipo de tarjeta')
    credit_Card = forms.CharField(widget=forms.TextInput(attrs={'style':'margin-left:100px', 'size':'50px','placeholder': 'Número de la tarjeta'}), label="")
    expired_Card = forms.CharField(widget=forms.TextInput(attrs={'style':'margin-left:100px', 'size':'50px','placeholder': 'Fecha de vencimiento de la tarjeta'}),label="")
    secCode_Card = forms.CharField(label="", widget=forms.PasswordInput(attrs={'style':'margin-left:100px', 'size':'50px','placeholder': 'Código de seguridad de la tarjeta'}))

    class Meta:
        model = User
        fields = [ "username", "first_name", "last_name", "password1", "password2", "credit_Card", "expired_Card", "secCode_Card", "subscription", "dni", "titular", "tipo_tarjeta"]

class configurarCuenta(forms.ModelForm):

    username =forms.EmailField(max_length=50, label='', widget=forms.TextInput(attrs={'style':'margin-left:100px', 'size':'50px','placeholder':'Dirección de correo electrónico'}))
    first_name = forms.CharField(max_length=30, label="", widget=forms.TextInput(attrs={'style':'margin-left:100px', 'size':'50px','placeholder': 'Nombre'}))
    last_name = forms.CharField(max_length=30, label="", widget=forms.TextInput(attrs={'style':'margin-left:100px', 'size':'50px','placeholder': 'Apellido'}))
    password1 = forms.CharField(label="", widget=forms.PasswordInput(attrs={'style':'margin-left:100px', 'size':'50px','placeholder': 'Contraseña'}))
    password2 = forms.CharField(label="", widget=forms.PasswordInput(attrs={'style':'margin-left:100px', 'size':'50px','placeholder': 'Confirmar contraseña'}))
    subscription = forms.ModelChoiceField(queryset=Membresia.objects.all(), label="Subscripción")
    titular = forms.CharField(label='', max_length=60, widget=forms.TextInput(attrs={'style':'margin-left:100px', 'size':'50px','placeholder': 'Nombre del titular de la tarjeta'}))
    dni = forms.CharField(label="", widget=forms.TextInput(attrs={'style':'margin-left:100px', 'size':'50px','placeholder': 'DNI del titular de la tarjeta'}))
    tipo_tarjeta = forms.ChoiceField(choices=[('Crédito', 'Crédito')]+[('Débito', 'Débito')], label='Tipo de tarjeta')
    credit_Card = forms.CharField(widget=forms.TextInput(attrs={'style':'margin-left:100px', 'size':'50px','placeholder': 'Número de la tarjeta'}), label="")
    expired_Card = forms.CharField(widget=forms.TextInput(attrs={'style':'margin-left:100px', 'size':'50px','placeholder': 'Fecha de vencimiento de la tarjeta'}),label="")
    secCode_Card = forms.CharField(label="", widget=forms.PasswordInput(attrs={'style':'margin-left:100px', 'size':'50px','placeholder': 'Código de seguridad de la tarjeta'}))
    class Meta:
        model = User
        fields = [ "username", "first_name", "last_name", "password1", "password2", "credit_Card", "expired_Card", "secCode_Card", "subscription", "titular", "dni", "tipo_tarjeta"]
