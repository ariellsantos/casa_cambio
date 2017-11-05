# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Moneda

# Register your models here.
@admin.register(Moneda)
class MonedaAdmin(admin.ModelAdmin):
    pass