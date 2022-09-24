from cProfile import Profile
from django import forms
from django.db import models
from django.contrib.auth.models import User
from django.forms import ModelForm


class Directorios(models.Model):
    nombre = models.CharField(max_length=250)
    contacto = models.CharField(max_length=250)

    def __str__(self):
        return f'Directorio : { self.nombre }'


class Administrativos(models.Model):
    nombre = models.CharField(max_length=250)
    cargo = models.CharField(max_length=250)


class Facultades(models.Model):
    nombre = models.CharField(max_length=250)
    escuelas = models.CharField(max_length=250)


class Avatar(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to='avatares', null=True, blank=True)
