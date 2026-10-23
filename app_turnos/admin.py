from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import EstadoTurno 
from .models import Rol
from .models import Especialidad 
from .models import Especialista
from .models import Paciente
from .models import Turno
from .models import AgendaDisponibilidad
from .models import Agenda
from .models import Configuracion
from .models import AuditoriaTurno
from .models import HistorialMedico
from .models import MiUsuario



# Register your models here.

@admin.register(MiUsuario)
class MiUsuarioAdmin(UserAdmin):
    model = MiUsuario

    fieldsets = UserAdmin.fieldsets + (
        ('Información Médica Adicional', {'fields': ('nombre', 'rut', 'telefono', 'fecha_nacimiento', 'rol', 'habilitado')}),
    )
    list_display = ('username', 'email', 'nombre', 'rut', 'is_staff')


admin.site.register(EstadoTurno)
admin.site.register(Rol) 
admin.site.register(Especialidad)
admin.site.register(Especialista)
admin.site.register(Paciente)
admin.site.register(Turno)
admin.site.register(AgendaDisponibilidad)
admin.site.register(Agenda)
admin.site.register(Configuracion)
admin.site.register(AuditoriaTurno)
admin.site.register(HistorialMedico)






