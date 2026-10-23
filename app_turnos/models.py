from django.db import models
from datetime import datetime
from django.contrib.auth.models import AbstractUser
int_habilitado = 1
fecha_creacion = datetime.now()
fecha_actualizacion = datetime.now()
str_codigo = "Código"
str_nombre = "Nombre"
str_descripcion = "Descripción"
str_www = "WWW"
str_email = "Email"
str_telefono = "Teléfono"
str_fecha_nac = "Fecha Nacimiento"
str_rut = "RUT"



  


    

class Rol(models.Model):
    nombre = models.CharField(str_nombre,max_length=50,null=False)
    descripcion = models.CharField(str_descripcion,max_length=255,null=True)
    habilitado = models.BooleanField(int_habilitado,default=True,null=False)
    created_at = models.DateTimeField(fecha_creacion,auto_now_add=True)
    updated_at = models.DateTimeField(fecha_actualizacion,auto_now=True)
    class Meta:
        db_table_comment = "Roles de usuario en el sistema médico (Administrador, Especialista, Paciente)."


class MiUsuario(AbstractUser):
    # Campos personalizados para tu centro médico (usando strings para los nombres visibles)
    nombre = models.CharField("Nombre", max_length=150, blank=True, null=True)
    rut = models.CharField("RUT", max_length=12, unique=True, null=True, blank=True)
    telefono = models.CharField("Teléfono", max_length=15, blank=True, null=True)
    fecha_nacimiento = models.DateField("Fecha de Nacimiento", blank=True, null=True)
    
    # Relación con el modelo Rol que ya tienes creado
    rol = models.ForeignKey(Rol, on_delete=models.PROTECT, null=True, blank=True)
    
    habilitado = models.BooleanField("Habilitado", default=True)

    def __str__(self):
        return self.username

    

class Especialidad(models.Model):
    nombre = models.CharField(str_nombre,max_length=100,null=False)
    descripcion = models.CharField(str_descripcion,max_length=255,null=True)
    habilitado = models.BooleanField(int_habilitado,default=True,null=False)
    created_at = models.DateTimeField(fecha_creacion,auto_now_add=True)
    updated_at = models.DateTimeField(fecha_actualizacion,auto_now=True)
    class Meta:
        db_table_comment = "Especialidades médicas disponibles en el centro de salud."

class Especialista(models.Model):
    usuario = models.ForeignKey(MiUsuario,on_delete=models.CASCADE,null=False)
    especialidad = models.ForeignKey(Especialidad,on_delete=models.PROTECT,null=False)
    registro_medico = models.CharField("Registro Médico",max_length=50,null=False)
    habilitado = models.BooleanField(int_habilitado,default=True,null=False)
    created_at = models.DateTimeField(fecha_creacion,auto_now_add=True)
    updated_at = models.DateTimeField(fecha_actualizacion,auto_now=True)
    class Meta:
        db_table_comment = "Datos profesionales de los especialistas médicos."

class Paciente(models.Model):
    usuario = models.ForeignKey(MiUsuario,on_delete=models.CASCADE,null=False)
    prevision = models.CharField("Previsión",max_length=50,null=True)
    habilitado = models.BooleanField(int_habilitado,default=True,null=False)
    created_at = models.DateTimeField(fecha_creacion,auto_now_add=True)
    updated_at = models.DateTimeField(fecha_actualizacion,auto_now=True)
    class Meta:
        db_table_comment = "Información clínica y de perfil de los pacientes."

class Configuracion(models.Model):
    especialista = models.ForeignKey(Especialista,on_delete=models.CASCADE,null=False)
    duracion_consulta = models.IntegerField("Duración Consulta (Minutos)",default=30,null=False)
    dias_atencion = models.CharField("Días de Atención",max_length=100,null=False)
    habilitado = models.BooleanField(int_habilitado,default=True,null=False)
    created_at = models.DateTimeField(fecha_creacion,auto_now_add=True)
    updated_at = models.DateTimeField(fecha_actualizacion,auto_now=True)
    class Meta:
        db_table_comment = "Configuración de parámetros para la gestión de agenda del especialista."

class AgendaDisponibilidad(models.Model):
    estado_disponibilidad = models.CharField("Estado Disponibilidad",max_length=30,null=False)
    descripcion = models.CharField(str_descripcion,max_length=255,null=True)
    habilitado = models.BooleanField(int_habilitado,default=True,null=False)
    created_at = models.DateTimeField(fecha_creacion,auto_now_add=True)
    updated_at = models.DateTimeField(fecha_actualizacion,auto_now=True)
    class Meta:
        db_table_comment = "Catálogo de estados posibles para los registros o bloques de la agenda."

class Agenda(models.Model):
    especialista = models.ForeignKey(Especialista,on_delete=models.CASCADE,null=False)
    configuracion = models.ForeignKey(Configuracion,on_delete=models.CASCADE,null=False)
    fecha_hora_inicio = models.DateTimeField("Fecha y Hora Inicio",null=False)
    fecha_hora_fin = models.DateTimeField("Fecha y Hora Fin",null=False)
    disponibilidad = models.ForeignKey(AgendaDisponibilidad,on_delete=models.PROTECT,null=False)
    habilitado = models.BooleanField(int_habilitado,default=True,null=False)
    created_at = models.DateTimeField(fecha_creacion,auto_now_add=True)
    updated_at = models.DateTimeField(fecha_actualizacion,auto_now=True)
    class Meta:
        db_table_comment = "Registros y bloques horarios que conforman la agenda de atención del especialista."

class EstadoTurno(models.Model):
    estado = models.CharField("Estado Turno",max_length=50,null=False)
    descripcion = models.CharField(str_descripcion,max_length=255,null=True)
    habilitado = models.BooleanField(int_habilitado,default=True,null=False)
    created_at = models.DateTimeField(fecha_creacion,auto_now_add=True)
    updated_at = models.DateTimeField(fecha_actualizacion,auto_now=True)
    class Meta:
        db_table_comment = "Catálogo de estados posibles para los turnos médicos."

class Turno(models.Model):
    paciente = models.ForeignKey(Paciente,on_delete=models.CASCADE,null=False)
    especialista = models.ForeignKey(Especialista,on_delete=models.CASCADE,null=False)
    fecha_hora = models.DateTimeField("Fecha y Hora Turno",null=False)
    estado = models.ForeignKey(EstadoTurno,on_delete=models.PROTECT,null=False)
    motivo_consulta = models.TextField("Motivo de Consulta",null=False)
    habilitado = models.BooleanField(int_habilitado,default=True,null=False)
    created_at = models.DateTimeField(fecha_creacion,auto_now_add=True)
    updated_at = models.DateTimeField(fecha_actualizacion,auto_now=True)
    class Meta:
        db_table_comment = "Registro de turnos y citas médicas agendadas."

class HistorialMedico(models.Model):
    turno = models.ForeignKey(Turno,on_delete=models.CASCADE,null=False)
    paciente = models.ForeignKey(Paciente,on_delete=models.CASCADE,null=False)
    especialista = models.ForeignKey(Especialista,on_delete=models.CASCADE,null=False)
    diagnostico = models.TextField("Diagnóstico",null=False)
    tratamiento = models.TextField("Tratamiento",null=False)
    observaciones = models.TextField("Observaciones",null=True)
    fecha_registro = models.DateTimeField("Fecha Registro",auto_now_add=True)
    habilitado = models.BooleanField(int_habilitado,default=True,null=False)
    created_at = models.DateTimeField(fecha_creacion,auto_now_add=True)
    updated_at = models.DateTimeField(fecha_actualizacion,auto_now=True)
    class Meta:
        db_table_comment = "Antecedentes históricos y diagnósticos clínicos de las consultas."

class AuditoriaTurno(models.Model):
    turno = models.ForeignKey(Turno,on_delete=models.CASCADE,null=False)
    estado_anterior = models.CharField("Estado Anterior",max_length=50,null=False)
    estado_nuevo = models.CharField("Estado Nuevo",max_length=50,null=False)
    modificado_por = models.ForeignKey(MiUsuario,on_delete=models.SET_NULL,null=True)
    comentario = models.TextField("Comentario Auditoría",null=True)
    fecha_cambio = models.DateTimeField("Fecha Cambio",auto_now_add=True)
    habilitado = models.BooleanField(int_habilitado,default=True,null=False)
    created_at = models.DateTimeField(fecha_creacion,auto_now_add=True)
    updated_at = models.DateTimeField(fecha_actualizacion,auto_now=True)
    class Meta:
        db_table_comment = "Registro de auditoría para el seguimiento de cambios de estado en turnos."