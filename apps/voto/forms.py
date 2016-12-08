from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import usuario, pregunta, opciones, pregunta_opcion, contestar_pregunta
from django.forms import ModelMultipleChoiceField
from django.forms import MultiWidget
from django.forms import widgets

class UserForm(UserCreationForm):
	nombre = forms.CharField(max_length=64)
	edad = forms.IntegerField()
	correo = forms.CharField(max_length=64)
	image= forms.ImageField()

class crear_preguntaForm(forms.ModelForm):
	class Meta:
		model = pregunta
		fields = '__all__'

class anadir_opcionesForm(forms.ModelForm):
	class Meta:
		model = opciones
		fields = '__all__'

class contestar_preguntaForm(forms.ModelForm):
	class Meta:
		model = contestar_pregunta
		fields = '__all__'
