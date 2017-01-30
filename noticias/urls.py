"""periodico URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from noticias import views

#from noticias.forms import NuevaNoticia
from django.views.generic import TemplateView

urlpatterns = [
    url(r'^$', views.noticias,name='noticias'),
    url(r'^gestion/nueva-noticia/$', views.nueva_noticia , name='nueva_noticia'),
    url(r'^gestion/modificar-noticia/$', views.modificarNoticia , name='modificarNoticia'),
    url(r'^gestion/nueva-seccion/$', views.nuevaSeccion , name='nuevaSeccion'),
    url(r'^gestion/eliminar-seccion/$', views.borrarSeccion , name='borrarSeccion'),
    url(r'^gestion/ver-secciones/$', views.ver_secciones , name='ver_secciones'),
    url(r'^gestion/eliminar-noticia/$', views.borrarNoticia , name='borrarNoticia'),


    url(r'^(?P<noticia_id>\d+)/', views.detail , name='noticiaAislada'),

    url(r'^seccion/(?P<seccion_name>\w+/$)', views.noticias_seccion , name='noticia_seccion'),

    url(r'^login/$', views.conectar, name='conectar'),
    url(r'^logout/$', views.desconectar, name='desconectar'),
    url(r'^registro/$', views.nuevoUsuario, name='nuevoUsuario'),

    url(r'^configuracion/eliminar-usuario/$', views.eliminarUsuario, name='eliminarUsuario'),
    url(r'^configuracion/cambiar-clave/$', views.cambiarClave , name='cambiarClave'),











]
