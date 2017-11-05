# -*- coding: utf-8 -*-
from __future__ import unicode_literals



from django.contrib.auth.decorators import login_required
from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages

from .models import Moneda,Monedero

from .forms import MonederoForm
from .monederos import crear_monedero, transferir_fondos_a_monedero
from .moneda import convertir_monto_a_moneda

@login_required
def index(request):
    usuario = request.user
    monederos = Monedero.objects.filter(usuario=usuario)
    context = {
        'usuario': usuario,
        'monederos': monederos,
    }

    return render(request, 'divisas/dashboard/index.html', context)


@login_required
def crear_monederos(request):
    if request.method == "POST":
        monedero_form = MonederoForm(request.POST)
        crear_monedero(request, monedero_form)
        messages.success(request, 'Se creo el monedero correctamente')
        return redirect("divisas:dashboard")
    elif request.method == "GET":
        form_monedero = MonederoForm()
        context = {
            'form_monedero': form_monedero,
        }
        return render(request, 'divisas/monederos/crear_monedero.html', context)

def fondear_monederos(request, pk):
    if request.method == "GET":
        monedero = Monedero.objects.get(pk=pk)
        moneda = monedero.moneda
        usuario = request.user

        context = {
            'monedero': monedero,
            'moneda': moneda,
            'usuario': usuario,
        }

        return render(request, 'divisas/monederos/fondear_monedero.html', context)
    elif request.method == "POST":
        monedero = Monedero.objects.get(pk=pk)
        usuario = request.user
        monto_a_transferir = convertir_monto_a_moneda(request, monedero)
        print "El monto a ransferir es {}".format(monto_a_transferir)
        monedero.monto = monedero.monto + monto_a_transferir
        transferir_fondos_a_monedero(request,monedero, usuario, monto_a_transferir)
        messages.success(request, 'Se transifirieron fondos al monedero correctamente')
        return redirect('divisas:dashboard')
