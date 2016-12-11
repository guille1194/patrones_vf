from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator
from django.core.urlresolvers import reverse
from django.core.validators import MaxValueValidator, MinValueValidator,MaxValueValidator
from django.utils import timezone
from multiselectfield import MultiSelectField
import datetime
# Create your models here.
class QuerySet(models.QuerySet):
	def get_categoria(self):
		return self.nombre

class usuario(models.Model):
	user_perfil = models.OneToOneField(User, related_name="profile")
	nombre = models.CharField(max_length=64)
	edad = models.IntegerField()
	correo = models.EmailField()

	def __unicode__(self):
		return '%s'%(self.user_perfil)

class categoria(models.Model):
	id= models.AutoField(primary_key=True)
	nombre = models.CharField(max_length=100)
	objects = QuerySet.as_manager()

	def __unicode__(self):
		return '%s' %(self.nombre)

class pregunta(models.Model):
	id = models.AutoField(primary_key=True)
	nombre = models.CharField(max_length=64)
	id_usuario = models.ForeignKey(usuario)
	id_categoria = models.ForeignKey(categoria,null=True,blank=True)
	creado = models.DateField(default=timezone.now,null=True,blank=True)


	def __unicode__(self):
		return '%s'%(self.nombre)

class opciones(models.Model):
	id = models.AutoField(primary_key=True)
	id_pregunta = models.ForeignKey(pregunta)
	opcion = models.CharField(max_length=64,null=True,blank=True)
	seleccionar = models.BooleanField(default=False)
	terminar = models.BooleanField(default=False)

	def __unicode__(self):
		return '%s'%(self.opcion)

class pregunta_opcion(models.Model):
	id = models.AutoField(primary_key=True)
	id_pregunta = models.ForeignKey(pregunta)
	id_opciones = models.ManyToManyField(opciones)
	creado = models.DateField(default=timezone.now,null=True,blank=True)

	def __unicode__(self):
		return u'%s'%(self.id)

	def get_opciones(self):
		return "\n".join([p.opcion for p in self.id_opciones.all()])
########################################################################### de aqui arriba funciona
class contestar_pregunta(models.Model):
	id = models.AutoField(primary_key=True)
	id_pregunta_opcion = models.ForeignKey(pregunta_opcion)
	id_opcion = models.ForeignKey(opciones,blank=True,null=True)

	def __unicode__(self):
		return '%s %s'%(self.id,self.id_opcion)

	#def get_opciones(self):
		return "\n".join([p.opcion for p in self.id_opcion.all()])
