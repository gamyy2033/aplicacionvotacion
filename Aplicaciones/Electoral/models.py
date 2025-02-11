from django.db import models
from django.core.exceptions import ValidationError
import re

# Validation function for Cedula (only 20 digits allowed)
def validate_cedula(value):
    if not re.match(r'^\d{10}$', value):
        raise ValidationError('La cédula debe tener exactamente 10 dígitos numéricos.')

# Validation function for letters-only fields
def validate_letters(value):
    if not value.isalpha():
        raise ValidationError('Este campo solo debe contener letras.')

class PartidoPolitico(models.Model):
    nombre = models.CharField(max_length=100, unique=True)
    siglas = models.CharField(max_length=10, unique=True)
    logo = models.ImageField(upload_to='partidos/', null=True, blank=True)

    def __str__(self):
        return self.nombre

class Cargo(models.Model):
    nombre = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.nombre

class Ubicacion(models.Model):
    nombre = models.CharField(max_length=100, unique=True)
    tipo = models.CharField(max_length=50, choices=[
        ('Provincia', 'Provincia'),
        ('Cantón', 'Cantón'),
        ('Parroquia', 'Parroquia')
    ])

    def __str__(self):
        return f"{self.nombre} ({self.tipo})"

class Recinto(models.Model):
    ubicacion = models.ForeignKey(Ubicacion, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

class Junta(models.Model):
    recinto = models.ForeignKey(Recinto, on_delete=models.CASCADE)
    numero = models.PositiveIntegerField()

    def __str__(self):
        return f"Junta {self.numero} - {self.recinto}"

class Candidato(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    partido = models.ForeignKey(PartidoPolitico, on_delete=models.CASCADE)
    cargo = models.ForeignKey(Cargo, on_delete=models.CASCADE)
    foto = models.ImageField(upload_to='candidatos/', null=True, blank=True)

    def __str__(self):
        return f"{self.nombre} {self.apellido} - {self.cargo.nombre} ({self.partido.siglas})"

    def clean(self):
        # Ensure only letters are allowed in nombre and apellido fields
        if not self.nombre.isalpha():
            raise ValidationError({'nombre': 'El nombre solo debe contener letras.'})
        if not self.apellido.isalpha():
            raise ValidationError({'apellido': 'El apellido solo debe contener letras.'})

class Votante(models.Model):
    cedula = models.CharField(max_length=10, unique=True, validators=[validate_cedula])  # 10 digits validation
    nombre = models.CharField(max_length=100, validators=[validate_letters])  # Letters only validation
    apellido = models.CharField(max_length=100, validators=[validate_letters])  # Letters only validation
    junta = models.ForeignKey(Junta, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.nombre} {self.apellido} ({self.cedula})"
