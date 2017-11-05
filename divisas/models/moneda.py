# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class Moneda(models.Model):
    """Model definition for Moneda."""

    nombre = models.CharField(max_length=50)
    nombre_corto = models.CharField(max_length=10)
    tipo_cambio = models.DecimalField(max_digits=11, decimal_places=2)

    class Meta:
        """Meta definition for Moneda."""

        verbose_name = 'Moneda'
        verbose_name_plural = 'Monedas'

    def __unicode__(self):
        """Unicode representation of Moneda."""
        return self.nombre
