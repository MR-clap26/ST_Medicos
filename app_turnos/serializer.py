from rest_framework import serializers
from .models import (
    Rol,
    MiUsuario,
    Especialidad,
    Especialista,
    Paciente,
    Configuracion,
    AgendaDisponibilidad,
    Agenda,
    EstadoTurno,
    Turno,
    HistorialMedico,
    AuditoriaTurno,
)

class RolSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rol
        fields = ('__all__')

class MiUsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = MiUsuario
        fields = ('__all__')

class EspecialidadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Especialidad
        fields = ('__all__')

class EspecialistaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Especialista
        fields = ('__all__')

class PacienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Paciente
        fields = ('__all__')

class ConfiguracionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Configuracion
        fields = ('__all__')

class AgendaDisponibilidadSerializer(serializers.ModelSerializer):
    class Meta:
        model = AgendaDisponibilidad
        fields = ('__all__')

class AgendaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Agenda
        fields = ('__all__')

class EstadoTurnoSerializer(serializers.ModelSerializer):
    class Meta:
        model = EstadoTurno
        fields = ('__all__')

class TurnoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Turno
        fields = ('__all__')

class HistorialMedicoSerializer(serializers.ModelSerializer):
    class Meta:
        model = HistorialMedico
        fields = ('__all__')

class AuditoriaTurnoSerializer(serializers.ModelSerializer):
    class Meta:
        model = AuditoriaTurno
        fields = ('__all__')

