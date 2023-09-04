from django.db import models

# Create your models here.
class Driver(models.Model):
    nome = models.CharField(max_length=120)
    data = models.CharField(max_length=50)
    cnh = models.CharField(max_length=2)

    def __str__(self):
        return self.nome

class Carros(models.Model):
    nome = models.CharField(max_length=50)
    placa = models.CharField(max_length=8)
    ano = models.CharField(max_length=4)
    cor = models.CharField(max_length=10)
    dono = models.CharField(max_length=20)

    def __str__(self):
        return self.nome