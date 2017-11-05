from decimal import Decimal
def convertir_monto_a_moneda(request, monedero):
    monto = Decimal(request.POST.get('transferir', 0))
    tipo_cambio = monedero.moneda.tipo_cambio
    monto_a_transferir = monto/tipo_cambio
    return monto_a_transferir