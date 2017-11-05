# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from .moneda import Moneda

class Monedero(models.Model):
    """Model definition for Monedero."""

    nombre = models.CharField(max_length=50)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    moneda = models.ForeignKey(Moneda, on_delete=models.CASCADE)
    monto = models.DecimalField(max_digits=11, decimal_places=2, default=0)

    class Meta:
        """Meta definition for Monedero."""

        verbose_name = 'Monedero'
        verbose_name_plural = 'Monederos'

    def __unicode__(self):
        """Unicode representation of Monedero."""
        return self.nombre
