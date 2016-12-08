import django
import sys
from .models import usuario

def user_image(request):
	try:
		img=None
		user=request.user
		up=usuario.objects.get(user_perfil=user)
		img='/media/%s'%up.image
	except:
		img='http://localhost:8000/media/debian.png'
	return img



def consultory(request):
	get_version_django = django.get_version()
	get_version_python = sys.version

	dic = { 'get_image_profile':user_image(request), 'django_version': get_version_django, 'python_version' : get_version_python}
	return dic