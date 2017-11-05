from decimal import Decimal

from .models.monedero import Monedero
from .models.moneda import Moneda

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
    usuario.perfil.fondo = usuario.perfil.fondo - fondo_a_tranferir
    usuario.perfil.save()
    return 200
    