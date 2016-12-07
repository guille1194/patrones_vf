from django.contrib import admin
from .models import usuario, pregunta, opciones, pregunta_opcion, contestar_pregunta
# Register your models here.
@admin.register(usuario)
class usuario_admin(admin.ModelAdmin):
	list_display = ('id','user_perfil','nombre','edad','correo')

@admin.register(pregunta)
class pregunta_admin(admin.ModelAdmin):
	list_display = ('id','nombre','id_usuario')

@admin.register(opciones)
class opciones_admin(admin.ModelAdmin):
	list_display = ('id','id_pregunta','opcion','seleccionar','terminar')

@admin.register(pregunta_opcion)
class pregunta_opcion_admin(admin.ModelAdmin):
	list_display = ('id','id_pregunta','get_opciones')

@admin.register(contestar_pregunta)
class contestar_pregunta_admin(admin.ModelAdmin):
	list_display = ('id','id_pregunta_opcion','id_opcion')