from django.urls import path, include
from rest_framework import routers
from . import views  # Reemplaza '. import views' con el nombre de tu app si es necesario

enrutador = routers.DefaultRouter()

enrutador.register(r'roles', views.RolViewSet)
enrutador.register(r'usuarios', views.MiUsuarioViewSet)
enrutador.register(r'especialidades', views.EspecialidadViewSet)
enrutador.register(r'especialistas', views.EspecialistaViewSet)
enrutador.register(r'pacientes', views.PacienteViewSet)
enrutador.register(r'configuraciones', views.ConfiguracionViewSet)
enrutador.register(r'agenda-disponibilidad', views.AgendaDisponibilidadViewSet)
enrutador.register(r'agendas', views.AgendaViewSet)
enrutador.register(r'estados-turno', views.EstadoTurnoViewSet)
enrutador.register(r'turnos', views.TurnoViewSet)
enrutador.register(r'historiales-medicos', views.HistorialMedicoViewSet)
enrutador.register(r'auditorias-turno', views.AuditoriaTurnoViewSet)

urlpatterns = [
    path('', include(enrutador.urls)),
]