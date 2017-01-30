from __future__ import unicode_literals

from django.db import models

from django.contrib.auth.models import User

# Create your models here.
#class Autor(models.Model):
    #name = models.CharField(max_length = 100)
#    descripcion = models.CharField(max_length = 300)
#    name = models.ForeignKey(User)

    #def __unicode__(self):
#    def __str__(self):
#        return self.name

class Seccion(models.Model):
    tipo = models.CharField(max_length = 100)
    def __unicode__(self):
        return self.tipo

class Noticia(models.Model):
    name = models.CharField(max_length = 300)
    autor = models.ForeignKey(User)
    breveDescripcion = models.CharField(max_length = 300)
    parrafo1 = models.CharField(max_length = 1000)
    parrafo2 = models.CharField(max_length = 1000, blank=True, null=True)
    parrafo3 = models.CharField(max_length = 1000, blank=True, null=True)
    parrafo4 = models.CharField(max_length = 1000, blank=True, null=True)
    parrafo5 = models.CharField(max_length = 1000, blank=True, null=True)
    parrafo6 = models.CharField(max_length = 1000, blank=True, null=True)
    fecha = models.DateTimeField(auto_now=True)
    fuente = models.CharField(max_length = 300)
    imagen = models.ImageField(upload_to = "noticias/static/photos/%Y/%m/%d",blank=True,null=True)
    seccion = models.ForeignKey(Seccion)

    def __unicode__(self):
        return self.name

    # Noticia = models.ForeignKey(Autor) para establecer relaciones 1-N

#class Usuario(models.Model):
#    user = models.CharField(max_length = 20)
#    def __unicode__(self):
#        return self.user

class Comentario(models.Model):
    usuario = models.ForeignKey(User)
    noticia = models.ForeignKey(Noticia, related_name = "Comentarios")
    fecha = models.DateTimeField(auto_now=True)
    descripcion = models.CharField(max_length = 300)

    def __unicode__(self):
        return self.descripcion
