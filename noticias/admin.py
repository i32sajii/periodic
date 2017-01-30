from django.contrib import admin
from noticias.models import Noticia, Seccion, Comentario #, Usuario , Autor
# Register your models here.
admin.site.register(Noticia)
#admin.site.register(Autor)
admin.site.register(Seccion)
#admin.site.register(Usuario)
admin.site.register(Comentario)
