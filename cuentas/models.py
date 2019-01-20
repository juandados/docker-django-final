from django.db import models

class Person(models.Model):
    id_type = models.CharField(max_length=10)
    id_number = models.CharField(max_length=20)
    name = models.CharField(max_length=20, unique=True)
    salary = models.FloatField()
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

class Cuenta(models.Model):
    person = models.ForeignKey('Person', on_delete=models.CASCADE)
    numero_cuenta = models.CharField(max_length=20)
    tipo = models.CharField(max_length=150)
    banco = models.CharField(max_length=150)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
