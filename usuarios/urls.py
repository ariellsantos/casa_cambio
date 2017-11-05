from django.conf.urls import url
from . import views

app_name = "usuarios"


urlpatterns = [
    url(r'logout/$', views.logout_user, name="logout" ),
    url(r'login/$', views.login_user, name="login"),
    url(r'crear_usuario/$', views.guardar_usuario, name="crear_usuario"),
    url(r'fondear_cuenta/$', views.fondear_cuenta_perfil, name="fondear_cuenta")
]