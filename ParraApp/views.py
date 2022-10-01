from django.shortcuts import render
from django.http import HttpResponse
from ParraApp.forms import CursoFormulario
from ParraApp.models import *
# Create your views here.

def inicio(request):
    
    return render(request,"ParraApp/inicio.html")

def curso(request):
    
    
    cur1 = Curso(nombre = "Sergio", camada = "2330")
    cur1.save()
    return render(request, "ParraApp/cursos.html")
    
    
def estudiante(request):
    
    return render(request, "ParraApp/estudiantes.html")

def profesor(request):
    
    return render(request, "ParraApp/profesores.html")

def entregable(request):
    
    return render(request, "ParraApp/entregables.html")

def cursoFormulario(request):
    
    if request.method== "POST":
        formulario1 = CursoFormulario(request.POST)
        
        if formulario1.is_valid():
            info = formulario1.cleaned_data
            curso = Curso(nombre=info["curso"], camada=info["camada"])
            
            curso.save()
            return render(request, "ParraApp/inicio.html")
    else:
        formulario1 = CursoFormulario()
        
    return render(request, "ParraApp/cursoFormulario.html", {"form1":formulario1})


def busquedaCamada(request):
    return render(request, "ParraApp/inicio.html")


def resultados(request):
    
    if request.GET["camada"]:
        
        camada = request.Get["camada"]
        cursos = Curso.objects.filter(camada__iexaxt=camada)
        
        return render(request, "ParraApp/inicio.html",{"cursos":cursos, "camada":camada})
        
    else:
        respuesta = "No enviaste datos."
        
    return HttpResponse(respuesta)

