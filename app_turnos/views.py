from django.shortcuts import render

from django.shortcuts import render
from rest_framework import viewsets

from .models import (
    MiUsuario,
    Rol,
    Especialidad,
    Especialista,
    Paciente,
    Configuracion,
    AgendaDisponibilidad,
    Agenda,
    EstadoTurno,
    Turno,
    HistorialMedico,
    AuditoriaTurno
)

from .serializer import (
    MiUsuarioSerializer,
    RolSerializer,
    EspecialidadSerializer,
    EspecialistaSerializer,
    PacienteSerializer,
    ConfiguracionSerializer,
    AgendaDisponibilidadSerializer,
    AgendaSerializer,
    EstadoTurnoSerializer,
    TurnoSerializer,
    HistorialMedicoSerializer,
    AuditoriaTurnoSerializer
)
# Create your views here.


class RolViewSet(viewsets.ModelViewSet):
    queryset = Rol.objects.all()
    serializer_class = RolSerializer

class MiUsuarioViewSet(viewsets.ModelViewSet):
    queryset = MiUsuario.objects.all()
    serializer_class = MiUsuarioSerializer

class EspecialidadViewSet(viewsets.ModelViewSet):
    queryset = Especialidad.objects.all()
    serializer_class = EspecialidadSerializer

class EspecialistaViewSet(viewsets.ModelViewSet):
    queryset = Especialista.objects.all()
    serializer_class = EspecialistaSerializer

class PacienteViewSet(viewsets.ModelViewSet):
    queryset = Paciente.objects.all()
    serializer_class = PacienteSerializer

class ConfiguracionViewSet(viewsets.ModelViewSet):
    queryset = Configuracion.objects.all()
    serializer_class = ConfiguracionSerializer

class AgendaDisponibilidadViewSet(viewsets.ModelViewSet):
    queryset = AgendaDisponibilidad.objects.all()
    serializer_class = AgendaDisponibilidadSerializer

class AgendaViewSet(viewsets.ModelViewSet):
    queryset = Agenda.objects.all()
    serializer_class = AgendaSerializer

class EstadoTurnoViewSet(viewsets.ModelViewSet):
    queryset = EstadoTurno.objects.all()
    serializer_class = EstadoTurnoSerializer

class TurnoViewSet(viewsets.ModelViewSet):
    queryset = Turno.objects.all()
    serializer_class = TurnoSerializer

class HistorialMedicoViewSet(viewsets.ModelViewSet):
    queryset = HistorialMedico.objects.all()
    serializer_class = HistorialMedicoSerializer

class AuditoriaTurnoViewSet(viewsets.ModelViewSet):
    queryset = AuditoriaTurno.objects.all()
    serializer_class = AuditoriaTurnoSerializer

def bienvenida(request):
    return render(request, 'bienvenida.html')

def home(request):
    return render(request, 'index.html')


def error_404(request, exception):
    return render(request, '404.html', status=404)


