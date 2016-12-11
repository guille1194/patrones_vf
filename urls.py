from django.conf.urls import url
from .views import *
from django.contrib.auth.views import login, logout_then_login
from django.contrib.auth.decorators import login_required

urlpatterns = [
	url(r'^login/$',login,{'template_name':'voto/login.html'}, name='login'),
	url(r'^logout/$', logout_then_login, name='logout'),
	url(r'^$',index_view,name='index_view'),
	url(r'^registro_usuario/$',registro_usuario.as_view(),name='registro_usuario'),
	url(r'^crear_pregunta/$',crear_pregunta,name='crear_pregunta'),
	url(r'^anadir_opciones/$',anadir_opciones,name='anadir_opciones'),
	url(r'^lista_preguntas/$',lista_preguntas,name='lista_preguntas'),
	url(r'^contestar_pregunta2/(?P<pk>[-\w]+)/$',contestar_pregunta2,name='contestar_pregunta2'),

]
