from django.contrib import admin
from django.utils.html import format_html

# Register your models here.

from .models import(Categoria,Projecto,ProjectoImagen,CategoriaImagen,Equipo,EquipoImagen,Cliente,ClienteImagen,InformacionIndex)

admin.site.register(Categoria)
admin.site.register(InformacionIndex)
#admin.site.register(Projecto)

@admin.register(Projecto)
class ProjectoAdmin(admin.ModelAdmin):
    list_display = ('nombre','categoria','departamente_ubicacion_projecto','distrito_ubicacion_projecto')
    list_filter = ('categoria','departamente_ubicacion_projecto')

@admin.register(ProjectoImagen)
class ProjectoImagenAdmin(admin.ModelAdmin):

    def imagen_html(self,obj):
        return format_html('<img src="{}" width=150px />'.format(obj.imagen.url))

    imagen_html.short_description = 'Imagen'

    list_display = ('orden','projecto', 'imagen_html')
    search_fields = ['projecto__nombre']

@admin.register(CategoriaImagen)
class CategoriaImagenAdmin(admin.ModelAdmin):

    def imagen_html(self,obj):
        return format_html('<img src="{}" width=150px />'.format(obj.imagen.url))

    imagen_html.short_description = 'Imagen Categoria'

    list_display= ('orden','categoria','imagen_html')
    search_fields = ['categoria__nombre']

@admin.register(Equipo)
class EquipoAdmin(admin.ModelAdmin):
    list_display = ('nombre','cargo')
    

@admin.register(EquipoImagen)
class EquipoImagenAdmin(admin.ModelAdmin):

    def imagen_html(self,obj):
        return format_html('<img src="{}" width=150px />'.format(obj.imagen.url))

    imagen_html.short_description = 'Foto del Equipo'

    list_display=('orden','equipo','imagen_html')

@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ('nombre','profesion')

@admin.register(ClienteImagen)
class ClienteImagenAdmin(admin.ModelAdmin):

    def imagen_html(self,obj):
        return format_html('<img src="{}" width=150px />'.format(obj.imagen.url))

    imagen_html.short_description = 'Foto del Cliente'

    list_display=('orden','cliente','imagen_html')

