from django.forms import ModelForm, Textarea
from django import forms
from noticias.models import Noticia, Seccion, Comentario

class NuevaNoticia(forms.ModelForm):
    class Meta:
        model = Noticia
        exclude=('',)

class LoginForm(forms.Form):
	usuario = forms.CharField(max_length=20)
	clave = forms.CharField(widget=forms.PasswordInput(), max_length=20)

class Registro(forms.Form):
	usuario = forms.CharField(max_length=20)
	clave = forms.CharField(widget=forms.PasswordInput(), max_length=20)
	repita_clave = forms.CharField(widget=forms.PasswordInput(), max_length=20)

class CambiarPass(forms.Form):
	user = forms.CharField(max_length=20)
	clave_antigua = forms.CharField(widget=forms.PasswordInput(), max_length=20)
	clave_nueva = forms.CharField(widget=forms.PasswordInput(), max_length=20)
	repita_la_nueva_clave = forms.CharField(widget=forms.PasswordInput(), max_length=20)

#class EliminarUsuario(forms.Form):
	#password = forms.CharField(max_length=30)

class FormularioSeccion(forms.Form):
	tipo = forms.CharField(max_length=100)

class EliminarNoticia(forms.Form):
	name = forms.CharField(max_length=300)
