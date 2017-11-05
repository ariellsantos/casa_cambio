from .models.perfil import Perfil

def fondear_cuenta(request, monto):
    perfil = Perfil.objects.get(usuario=request.user)
    perfil.fondo = perfil.fondo + monto
    perfil.save()
    return 200
