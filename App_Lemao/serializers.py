from rest_framework import serializers
from django.db.models import Avg
from .models import *

class DriverSerializer(serializers.ModelSerializer):
    class Meta:
        model = Driver
        fields = (
            'nome',
            'data',
            'cnh',
        )

class CarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = (
            'nome',
            'placa',
            'ano',
            'cor',
            'dono',
        )

class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = (
            'servico',
            'descricao',
            'icone',
        )

class RoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Role
        fields = (
            'cargo',
        )

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = (
            'nome',
            'cargo',
            'bio',
            'imagem',
            'facebook',
            'twitter',
            'instagram',
        )

class ScheduleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Schedule
        fields = (
            'motorista',
            'data',
            'carro',
            'dia',
        )