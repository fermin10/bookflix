
from django import forms
from .models import Perfil


class crearPerfil(forms.ModelForm):
    nombre = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Nombre del perfil'}), max_length=30, label="")

    class Meta:
        model = Perfil
        fields = ["nombre"]
        exclude = ["usuario"]

