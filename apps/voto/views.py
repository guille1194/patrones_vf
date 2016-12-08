from django.shortcuts import render, get_object_or_404, redirect, render_to_response
from django.views.generic import FormView, CreateView, ListView,DetailView,UpdateView,DeleteView
from .forms import  UserForm, crear_preguntaForm, anadir_opcionesForm, contestar_preguntaForm
from django.core.urlresolvers import reverse_lazy
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from .models import usuario, pregunta, opciones, pregunta_opcion, contestar_pregunta
from django.core.paginator import Paginator, EmptyPage, InvalidPage, PageNotAnInteger
from django.views.generic.detail import SingleObjectMixin
from django.contrib.auth.models import User
from django.views.generic.edit import ModelFormMixin
from decimal import Decimal  

# Create your views here.
def index_view(request):
	pre = pregunta.objects.all()
	ctx = {'instance':pre}
	return render(request,'voto/index.html',ctx)

class registro_usuario(FormView):
	template_name = 'voto/registro_usuario.html'
	form_class = UserForm
	success_url = reverse_lazy('index_view')

	def form_valid(self,form):
		user = form.save()
		p = usuario()
		p.user_perfil = user
		p.nombre = form.cleaned_data['nombre']
		p.edad = form.cleaned_data['edad']
		p.correo = form.cleaned_data['correo']
		p.save()
		return super(registro_usuario,self).form_valid(form)

def crear_pregunta(request):
	form = crear_preguntaForm(request.POST or None)
	if form.is_valid():
		instance = form.save(commit=False)
		instance.save()
		return redirect('anadir_opciones')
	return render(request,'voto/crear_pregunta.html')

def anadir_opciones(request,pk=None):
	pregunta_get = pregunta.objects.latest('id')
	all_opciones = opciones.objects.filter(id_pregunta=pregunta_get)
	listaop = []

	for i in all_opciones:
		listaop.append(i)

	form = anadir_opcionesForm(request.POST or None)
	if form.is_valid():
		instance = form.save()
		instance.id_pregunta = pregunta.objects.get(id=request.POST['id_pregunta'])
		instance.opcion = request.POST['opcion']
		instance.save()
		if instance.terminar == True:
			p = pregunta_opcion()
			p.id_pregunta = instance.id_pregunta
			p.save()
			p.id_opciones = listaop
			return redirect('index_view')
	else:
		print "no valido"
	return render(request,'voto/anadir_opciones.html',{"object":pregunta_get})

def contestar_pregunta(request,pk=None):
	insta = get_object_or_404(pregunta,id=pk)
	preop = pregunta_opcion.objects.filter(id_pregunta = insta.id)
	ctx = {
			"object":insta,
			"list_objects":preop,
	}
	form = contestar_preguntaForm(request.POST or None)
	if form.is_valid():
		instance = form.save()
		print instance.id_opcion
		instance.save()
		return redirect('index_view')

	return render(request,'voto/contestar_pregunta.html',ctx)





