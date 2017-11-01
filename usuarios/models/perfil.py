# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

class Perfil(models.Model):
    """Model definition for Perfil."""

    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    direccion = models.CharField(max_length=350)
    telefono = models.CharField(max_length=14)
    fondo = models.DecimalField(max_digits=11, decimal_places=3, default=0)

    class Meta:
        """Meta definition for Perfil."""

        verbose_name = 'Perfil'
        verbose_name_plural = 'Perfiles'

    def __unicode__(self):
        """Unicode representation of Perfil."""
        return self.usuario.first_name
