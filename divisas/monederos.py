from decimal import Decimal

from threading import Thread
import requests
from .models.monedero import Monedero
from .models.moneda import Moneda
from django.conf import settings

def crear_monedero(request, form):
    if form.is_valid():
        nombre = form.cleaned_data['nombre']
        moneda = form.cleaned_data['moneda']
        usuario = request.user
        monedero = Monedero(nombre=nombre, moneda=moneda, usuario=usuario)
        monedero.save()
    return 200

def transferir_fondos_a_monedero(request, monedero,usuario, monto_a_transferir):
    fondo_a_tranferir = Decimal(request.POST.get('transferir',0))
    print "Monto a transferir {}".format(monto_a_transferir)
    monedero.monto + monto_a_transferir
    monedero.save()
    message = "Se ha fondeado el monedero {} con la cantidad de {} <span style='color:green;'>{}</span>".format(monedero.nombre, monto_a_transferir, monedero.moneda.nombre_corto)
    hilo = Thread(target=_send_email, args=(request.user.email, message))
    hilo.start()
    usuario.perfil.fondo = usuario.perfil.fondo - fondo_a_tranferir
    usuario.perfil.save()
    return 200
    

def _send_email(email, message):
    print settings.MAILGUN_KEY
    email_sent = requests.post(
        "https://api.mailgun.net/v3/correo.com/messages",
        auth=("api", settings.MAILGUN_KEY),
        data={"from": "Casa de cambio SA de VB. <hola@correo.com>",
              "to": [email],
              "subject": "Mensaje de la casa de cambio",
              "html": message,
              "o:tracking:": True})
    
    print email_sent.status_code
    print "Hola"
    return email_sent