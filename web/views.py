from django.shortcuts import render
from .models import(Categoria,CategoriaImagen,Projecto,ProjectoImagen)

# Create your views here.
def index(request):
    lista_categorias = Categoria.objects.all()
    proyecto_lista_a = Projecto.objects.filter(categoria_id__id= 1)[:3]
    proyecto_lista_b = Projecto.objects.filter(categoria_id__id= 2)[:3]

    context = {
        'categorias': lista_categorias,
        'instalaciones': proyecto_lista_a,
        'metales': proyecto_lista_b
    }

    return render(request,'index.html',context)

def about(request):
    return render(request,'about.html')

def contacto(request):
    return render(request,'contact.html')

def proyectos(request):
    return render(request,'project.html')

def servicios(request):
    return render(request,'service.html')

def equipo(request):
    return render(request,'team.html')

def testimonio(request):
    return render(request,'testimonial.html')

