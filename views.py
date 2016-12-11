from django.shortcuts import render, get_object_or_404, redirect, render_to_response
from django.views.generic import FormView, CreateView, ListView,DetailView,UpdateView,DeleteView
from .forms import  UserForm, crear_preguntaForm, anadir_opcionesForm, contestar_preguntaForm
from django.core.urlresolvers import reverse_lazy
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from .models import usuario, pregunta, opciones, pregunta_opcion, contestar_pregunta, categoria
from django.core.paginator import Paginator, EmptyPage, InvalidPage, PageNotAnInteger
from django.views.generic.detail import SingleObjectMixin
from django.contrib.auth.models import User
from django.views.generic.edit import ModelFormMixin
from decimal import Decimal
from django.contrib.auth.decorators import login_required
import datetime



# Create your views here.
def index_view(request):
	return render(request,"voto/index.html")

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

@login_required(login_url='/login')
def crear_pregunta(request):
	form = crear_preguntaForm(request.POST or None,request.FILES or None)
	c = categoria.objects.all()
	ctx = {'categorias':c}
	if form.is_valid():
		instance = form.save(commit=False)
		instance.creado = datetime.datetime.now()
		instance.save()
		return redirect('anadir_opciones')
	return render(request,'voto/crear_pregunta.html',ctx)

@login_required(login_url='/login')
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

@login_required(login_url='/login')
def contestar_pregunta2(request,pk=None):
	insta = get_object_or_404(pregunta,id=pk)
	preop = pregunta_opcion.objects.filter(id_pregunta = insta.id)
	p = contestar_pregunta.objects.all()

	for i in p:
		cesar = i.id_pregunta_opcion
		#print cesar


	print p

	ctx = {
			"object":insta,
			"object_list":preop,
	}

	form = contestar_preguntaForm(request.POST or None)
	if form.is_valid():
		instance = form.save()
		print instance.id_opcion
		instance.save()
		return redirect('index_view')

	return render(request,'voto/contestar_pregunta.html',ctx)

@login_required(login_url='/login')
def lista_preguntas(request):
	queryset_list = pregunta.objects.all().order_by('-creado')
	paginator = Paginator(queryset_list, 3) # Show 3 contacts per page
	page = request.GET.get('page')
	try:
		queryset = paginator.page(page)
	except PageNotAnInteger:
		# If page is not an integer, deliver first page.
		queryset = paginator.page(1)

	except EmptyPage:
		# If page is out of range (e.g. 9999), deliver last page of results.
		queryset = paginator.page(paginator.num_pages)
	context = {
		'object_list': queryset_list
	}
	return render(request, "voto/lista_preguntas.html", context)


	def resultados(request):
		return (request,'voto/index.html')
