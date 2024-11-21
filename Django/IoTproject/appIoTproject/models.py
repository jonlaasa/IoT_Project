from django.db import models

class Paciente(models.Model):
    id = models.CharField(max_length=100, primary_key=True)
    nombre = models.CharField(max_length=100,default='name')
    apellido = models.CharField(max_length=100,default='firstname')
    hear_rate = models.IntegerField()
    o2_sangre = models.DecimalField(max_digits=5, decimal_places=2)
    temperatura_corporal = models.DecimalField(max_digits=4, decimal_places=1)
    tiempo_tomado = models.DateTimeField()
    direccion = models.CharField(max_length=255)

    def __str__(self):
        return f'Paciente {self.nombre} {self.apellido} ({self.id})'

class Familiar(models.Model):
    id = models.CharField(max_length=100, primary_key=True)
    nombre = models.CharField(max_length=100,default='name')
    apellido = models.CharField(max_length=100, default='firstname')
    usuario = models.CharField(max_length=100, unique=True, default='user')
    contraseña = models.CharField(max_length=128, default='contra')  # Usualmente hashed en la base de datos

    def __str__(self):
        return f'{self.nombre} {self.apellido} ({self.id})'

class PacienteFamiliarUnion(models.Model):
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)
    familiar = models.ForeignKey(Familiar, on_delete=models.CASCADE)

    def __str__(self):
        return f'Union - Paciente {self.paciente.id} - Familiar {self.familiar.id}'
