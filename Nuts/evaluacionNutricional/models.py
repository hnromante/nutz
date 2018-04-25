from django.db import models
from django.contrib.auth import get_user_model #User
# Create your models here.

# ==============================================================================
# MODELOS DE USUARIOS
# ==============================================================================
class Paciente(models.Model):
    user = models.ForeignKey(get_user_model, on_delete=models.CASCADE)

class Nutricionista(models.Model):
    user = models.ForeignKey(get_user_model, on_delete=models.CASCADE)

class Administrador(models.Model):
    user = models.ForeignKey(get_user_model, on_delete=models.CASCADE)

# ==============================================================================
# MODELO FICHA PACIENTE
# ==============================================================================
class Ficha_paciente(models.Model):
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)

# ==============================================================================
# MODELO FICHA ANAMNESIS
# ==============================================================================
class Ficha_anamnesis(models.Model):
    paciente = models.ForeignKey(Paciente,on_delete= models.CASCADE)
    tabaco_frecuencia = models.IntegerField() 
    alcohol_frecuencia = models.IntegerField()
    drogas_frecuencia = models.IntegerField()
    actividad_fisica_frecuencia = models.IntegerField()

class Antecedentes_medicos(models.Model):
    paciente = models.ForeignKey(Paciente,on_delete= models.CASCADE)

    patologias = models.IntegerField()
    detalle_patologia = models.CharField()
    condicion_general = models.CharField(choices=()) #TUPLA CONDICIONES GENERALES

    cefaleas = models.BooleanField()
    mareos = models.BooleanField()
    calambres = models.BooleanField()
    tinitus = models.BooleanField()
    parestesia = models.BooleanField()
    angor = models.BooleanField()
    crisis_hta = models.BooleanField()
    acv = models.BooleanField()
    iam = models.BooleanField()
    descompensacion_dm = models.BooleanField()
    diuresis = models.BooleanField()
    nicturia = models.BooleanField()
    poliuria = models.BooleanField()
    polifagia = models.BooleanField()
    polidipsia = models.BooleanField()
    xerostomia = models.BooleanField()
    
    hospitalizaciones = models.CharField() #BOOL?
    alergias_farmacos = models.CharField() #BOOL?
    cirugias = models.CharField() #BOOL?
    automedicacion = models.CharField() #BOOL?

    observacion = models.CharField()

class Ficha_evaluacion_nutricional(models.Model):
    paciente = models.ForeignKey(Paciente, on_delete=models.Model)

class Ficha_params_bioquimicos(models.Model):
    paciente = models.ForeignKey(Paciente, on_delete=models.Model)




# ==============================================================================
# MODELOS DE ALIMENTOS
# ==============================================================================
class Tipo_alimiento(models.Model):
    nombre = models.CharField()

class Alimento(models.Model):
    tipo_alimento = models.ForeignKey(Tipo_alimiento,on_delete=models.CASCADE)