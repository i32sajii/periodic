from django.shortcuts import render
from django.http import HttpResponseRedirect
from noticias.models import Noticia, Seccion, Comentario #, Usuario , Aut
from django.template import RequestContext, loader
from django.views.generic.edit import CreateView
from noticias.forms import NuevaNoticia, LoginForm, Registro, CambiarPass, FormularioSeccion, EliminarNoticia #EliminarUsuario,
from django.core.urlresolvers import reverse, reverse_lazy
from django.views.generic import TemplateView
from django.views.generic import ListView
from django.shortcuts import get_object_or_404
from django.views.generic.edit import FormView
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import auth
import time
# Create your views here.
def noticias(request):
    lista=Noticia.objects.all()
    return render(request, 'noticias/noticias.html', {'lista': lista} )


def nueva_noticia(request):
  messageOk = None
  if request.method=="POST":
    form= NuevaNoticia(request.POST)
    if form.is_valid():
      name = request.POST['name']
      autor = request.POST['autor']
      breveDescripcion = request.POST['breveDescripcion']
      parrafo1 = request.POST['parrafo1']
      parrafo2 = request.POST['parrafo2']
      parrafo3 = request.POST['parrafo3']
      parrafo4 = request.POST['parrafo4']
      parrafo5 = request.POST['parrafo5']
      parrafo6 = request.POST['parrafo6']
      fuente = request.POST['fuente']
      imagen = request.POST['imagen']
      seccion = request.POST['seccion']
      newNoticia = form.save(commit=False)
      newNoticia.save()
      messageOk = "Noticia creada correctamente."
  else:
    form=NuevaNoticia()
  return render(request, 'noticias/nuevaNoticia.html',{'messageOk': messageOk, 'form':form,})

  #NoticiaAislada
def detail(request, noticia_id):
	noticiaDatos = Noticia.objects.all().filter(id=int(noticia_id))
	comentario = Comentario.objects.all().filter(noticia=int(noticia_id))
	for n in noticiaDatos:
		imagenRuta = getattr(n, 'imagen')
	return render(request, 'noticias/noticiaAislada.html', {'noticiaDatos': noticiaDatos, 'comentario': comentario, 'imagenRuta': str(imagenRuta)[8:],} )

def noticias_seccion(request, seccion_name):
    seccion = Seccion.objects.all().filter(tipo=str(seccion_name[:-1]))

    for s in seccion:
        identificador = s.id
    seccion_lista = Noticia.objects.all().filter(seccion=int(identificador))

    return render(request, 'noticias/seccionNoticia.html', {'seccion_lista': seccion_lista, 'seccion_name': seccion_name[:-1],})

@login_required(login_url='/noticias/login/')
def desconectar(request):
    logout(request)
    return HttpResponseRedirect("/noticias/")

def conectar(request):
	messageOk = None
	messageFail = None
	messageWarning = None
	if request.method == "POST":
		form = LoginForm(request.POST)
		if form.is_valid():
			username = request.POST['usuario']
			password = request.POST['clave']
			user = authenticate(username=username, password = password)
			if user is not None:
				if user.is_active:
					login(request, user)
					messageOk = "Identificado correctamente."
				else:
					messageWarning = "Tu usuario se encuentra desactivado."
			else:
				messageFail= "Nombre de usuario y/o clave incorrectos."
	else:
		form = LoginForm()

	return render(request, 'noticias/login.html', {'messageOk': messageOk, 'messageFail': messageFail, 'messageWarning': messageWarning, 'form': form,})


def nuevoUsuario(request):
	messageOk = None
	messageFail= None
	if request.method == "POST":
		form = Registro(request.POST)
		if form.is_valid:
			username = request.POST['usuario']
			password1 = request.POST['clave']
			password2 = request.POST['repita_clave']
			user_old = User.objects.filter(username = username)
			if password1 == password2:
				if user_old.exists():
					messageFail = "El nombre de usuario coincide con uno ya existente."
				else:
					user = User.objects.create_user(username, '', password1)
					user.save()
					#Cada vez que creemos un usuario, crearemos un Usuario.
					messageOk = "Usuario creado correctamente."
			else:
				messageFail = "Las claves no coinciden."
	else:
		form = Registro()
	return render(request, 'noticias/nuevoUsuario.html', {'messageOk': messageOk, 'messageFail':messageFail, 'form': form})


@login_required(login_url='/noticias/login/')
def cambiarClave(request):
	messageOk = None
	messageFail = None
	usuarioLogIn = request.user
	if request.method == "POST":
		form = CambiarPass(request.POST)
		if form.is_valid():
			username = request.POST['user']
			clave_antigua = request.POST['clave_antigua']
			clave_nueva = request.POST['clave_nueva']
			repita_la_nueva_clave = request.POST['repita_la_nueva_clave']
			if str(usuarioLogIn) == str(request.user.username):
				if clave_nueva == repita_la_nueva_clave:
					user = authenticate(username = username, password = clave_antigua)
					if user is not None:
						if user.is_active:
							usuarioLogIn.set_password(clave_nueva)
							usuarioLogIn.save()
							messageOk = "Clave cambiada correctamente."
					else:
						messageFail = "Vaya... parece que ha habido un error..."
				else:
					messageFail = "ERROR. Las claves nuevas no coinciden entre ellas."
			else:
				messageFail = "Vaya... parece que ha habido un error con el nombre de usuario..."
	else:
		form = CambiarPass()
        return render(request, 'noticias/cambiarClave.html', {'messageOk': messageOk, 'messageFail':messageFail, 'form': form})




@login_required(login_url='/noticias/login/')
def eliminarUsuario(request):
    messageOk = None
    messageFail = None
    usuarioLogIn = request.user
    if request.method == "POST":
        user_old = User.objects.filter(username = usuarioLogIn)
        user_old.delete()
        messageOk = "Su usuario se ha eliminado correctamente."
    return render(request, 'noticias/eliminarUsuario.html', {'messageOk': messageOk})



@login_required(login_url='/noticias/login/')
def modificarNoticia(request):
	messageOk = None
	messageFail = None
	if request.method == "POST":
		form = NuevaNoticia(request.POST)
		if form.is_valid():
			name = request.POST['name']
			autor = request.POST['autor']
			breveDescripcion = request.POST['breveDescripcion']
			parrafo1 = request.POST['parrafo1']
			parrafo2 = request.POST['parrafo2']
			parrafo3 = request.POST['parrafo3']
			parrafo4 = request.POST['parrafo4']
			parrafo5 = request.POST['parrafo5']
			parrafo6 = request.POST['parrafo6']
			fuente = request.POST['fuente']
			imagen = request.POST['imagen']
			seccion = request.POST['seccion']
			noticia_nueva = Noticia.objects.filter(name = name)
			if noticia_nueva.exists():
				#noticia_nueva.delete()
				noticia_vieja = Noticia.objects.get(name = name)
				noticia_vieja.name = name
				noticia_vieja.autor = User.objects.get(id = str(autor))
				noticia_vieja.breveDescripcion = request.POST['breveDescripcion']
				noticia_vieja.parrafo1 = parrafo1
				noticia_vieja.parrafo2 = parrafo2
				noticia_vieja.parrafo3 = parrafo3
				noticia_vieja.parrafo4 = parrafo4
				noticia_vieja.parrafo5 = parrafo5
				noticia_vieja.parrafo6 = parrafo6
				noticia_vieja.fuente = fuente
				noticia_vieja.imagen = imagen
				noticia_vieja.seccion = Seccion.objects.get(id = str(seccion))
				noticia_vieja.save()
				messageOk = "Noticia modificada correctamente."
			else:
				messageFail = "Esta noticia no existe."
	else:
		form = NuevaNoticia()
	return render(request, 'noticias/nuevaNoticia.html', {'messageOk': messageOk, 'messageFail':messageFail, 'form':form,})


@login_required(login_url='/noticias/login/')
def borrarNoticia(request):
	messageOk = None
	messageFail = None
	if request.method == "POST":
		form = EliminarNoticia(request.POST)
		if form.is_valid():
			name = request.POST['name']
			noticia_old = Noticia.objects.filter(name = name)
			if noticia_old.exists():
				noticia_old.delete()
				messageOk = "Noticia eliminada correctamente."
			else:
				messageFail = "Esta noticia no existe."
	else:
		form = EliminarNoticia()
	return render(request, 'noticias/eliminarNoticia.html', {'messageOk': messageOk, 'messageFail':messageFail, 'form':form,})






@login_required(login_url='/noticias/login/')
def nuevaSeccion(request):
	messageOk = None
	messageFail = None
	if request.method == "POST":
		form = FormularioSeccion(request.POST)
		if form.is_valid():
			tipo = request.POST['tipo']
			seccion_old = Seccion.objects.filter(tipo = tipo)
			if seccion_old.exists():
				messageFail = "Ya existe esta seccion."
			else:
				seccion = Seccion(tipo = tipo)
				seccion.save()
				messageOk = "Se ha creado esta seccion correctamente."
	else:
		form = FormularioSeccion()
	return render(request, 'noticias/nuevaSeccion.html', {'messageOk': messageOk, 'messageFail':messageFail, 'form':form,})

@login_required(login_url='/noticias/login/')
def borrarSeccion(request):
	messageOk = None
	messageFail = None
	if request.method == "POST":
		form = FormularioSeccion(request.POST)
		if form.is_valid():
			tipo = request.POST['tipo']
			seccion_old = Seccion.objects.filter(tipo = tipo)
			if seccion_old.exists():
				seccion_old.delete()
				messageOk = "Seccion eliminada correctamente."
			else:
				messageFail = "Esta seccion no existe."
	else:
		form = FormularioSeccion()
	return render(request, 'noticias/nuevaSeccion.html', {'messageOk': messageOk, 'messageFail':messageFail, 'form':form,})
    #                              reutilizo nueva para borrar

def ver_secciones(request):
    secciones_list = Seccion.objects.order_by('id')
    return render(request, 'noticias/verSeccion.html', {'secciones_list': secciones_list,})
