from django.db import models

class Paciente(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    edad = models.IntegerField()
    fecha_nacimiento = models.DateField()

    def __str__(self):
        return f"{self.nombre} {self.apellido}"

class Doctor(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    edad = models.IntegerField()
    fecha_nacimiento = models.DateField()
    especialidad = models.CharField(max_length=100)

    def __str__(self):
        return f"Dr. {self.nombre} {self.apellido}"

class HoraMedica(models.Model):
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    hora = models.TimeField()
    fecha = models.DateField()
    motivo = models.TextField()

    def __str__(self):
        return f"{self.fecha} {self.hora} - {self.paciente}"