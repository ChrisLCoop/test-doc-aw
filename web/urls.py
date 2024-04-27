from django.urls import path
from . import views

app_name='web'

urlpatterns = [
    path('',views.index,name='index'),
    path('about',views.about,name='acerca_de'),
    path('contacto',views.contacto,name='contacto'),
    path('proyectos',views.proyectos,name='proyectos'),
    path('servicios',views.servicios,name='servicios'),
    path('team',views.equipo,name='equipo'),
    path('testimonial',views.testimonio,name='testimonio'),
]