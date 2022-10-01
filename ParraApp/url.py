from django.urls import path
from ParraApp.views import *

urlpatterns = [
    path("", inicio, name="Inicio"),
    path("cursos/", curso, name="Curso"),
    path("profesor/", profesor, name="Profesores"),
    path("estudiantes/", estudiante, name="Estudiante"),
    path("entregables/", entregable, name="Entregables"),
    path("cursoFormulario/", cursoFormulario, name="FormularioCurso"),
    path("buscarCamada/", busquedaCamada, name="BuscarCamada"),
    path("resultados/", resultados, name="ResultadosBusqueda"),
]