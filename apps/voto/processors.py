import django
import sys
from django.shortcuts import render, get_object_or_404, redirect, render_to_response
from .models import usuario, pregunta

def user_image(request):
	try:
		img=None
		user=request.user
		up=usuario.objects.get(user_perfil=user)
		img='/media/%s'%up.image
	except:
		img='http://localhost:8000/media/debian.png'
	return img

#def pregunta_image(request,pk=None):
#	try:
#		img=None
#		current_preguntas = request.pregunta#get_object_or_404(pregunta,id=pk)
#		up=pregunta.objects.get(id=current_preguntas)
#		img = '/media/%s'%up.image
#		print pk
#	except:
#		img='http://localhost:8000/media/Preguntas/a.jpg'
#	return img




def consultory(request):
	dic = { 
			'get_image_profile':user_image(request),
			#'get_image_pregunta':pregunta_image(request,pk=None)
	}
	return dic