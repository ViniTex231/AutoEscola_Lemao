from django.db import models
from stdimage.models import StdImageField
import uuid

# Create your models here.

def get_file_path(_instance, filename):
    ext = filename.split('.')[-1]
    filename = f'{uuid.uuid4()}.{ext}'
    return filename

class Driver(models.Model):
    nome = models.CharField(max_length=120)
    data = models.CharField(max_length=50)
    cnh = models.CharField(max_length=2)

    class Meta:
        verbose_name = 'Driver'
        verbose_name_plural = 'Drivers'

    def __str__(self):
        return self.nome

class Car(models.Model):
    nome = models.CharField(max_length=50)
    placa = models.CharField(max_length=8)
    ano = models.CharField(max_length=4)
    cor = models.CharField(max_length=10)
    dono = models.CharField(max_length=20)

    class Meta:
        verbose_name = 'Car'
        verbose_name_plural = 'Cars'

    def __str__(self):
        return self.nome
    
class Base(models.Model):
    criados = models.DateField('Criação', auto_now_add=True)
    modificado = models.DateField('Atualização', auto_now=True)
    ativo = models.BooleanField('Ativo?', default=True)

    class Meta:
        abstract = True

class Service(Base):
    ICONE_CHOICES = (
        ('lni-car', 'Carro'),
        ('lni-bus', 'Onibus'),
        ('lni-train', 'Trem'),
    )
    servico = models.CharField('Serviço', max_length=100)
    descricao = models.TextField('Descrição', max_length=200)
    icone = models.CharField('Icone', max_length=12, choices=ICONE_CHOICES)

    class Meta:
        verbose_name = 'Service'
        verbose_name_plural = 'Services'

    def __str__(self):
        return self.servico
    
class Role(Base):
    cargo = models.CharField('Cargo', max_length=100)

    class Meta:
        verbose_name = 'Role'
        verbose_name_plural = 'Roles'

    def __str__(self):
        return self.cargo
    
class Employee(Base):
    nome = models.CharField('Nome', max_length=100)
    cargo = models.ForeignKey('App_Lemao.Role', verbose_name='Role', on_delete=models.CASCADE)
    bio = models.TextField('Bio', max_length=200)
    imagem = StdImageField('Imagem', upload_to=get_file_path, variations={'thumb': {'width': 480, 'height': 480, 'crop': True}})
    facebook = models.CharField('Facebook', max_length=100, default='#')
    twitter = models.CharField('Twitter', max_length=100, default='#')
    instagram = models.CharField('Instagram', max_length=100, default='#')

    class Meta:
        verbose_name = 'Employee'
        verbose_name_plural = 'Employees'

    def __str__(self):
        return self.nome
    
class Schedule(Base):
    DIAS = (
        ('segunda', 'Segunda'),
        ('terca', 'Terça'),
        ('quarta', 'Quarta'),
        ('quinta', 'Quinta'),
        ('sexta', 'Sexta'),
    )
    motorista = models.ForeignKey('Driver', on_delete=models.CASCADE)
    data = models.DateField()
    carro = models.ForeignKey('Car', on_delete=models.CASCADE)
    dia = models.CharField('Dia', max_length=7, choices=DIAS)

    class Meta:
        verbose_name = 'Schedule'
        verbose_name_plural = 'Schedules'
    

    def __str__(self) -> str:
        return f'{self.motorista} {self.data} {self.carro} {self.dia}'
