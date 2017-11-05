from django.conf.urls import url
from . import views

app_name = "divisas"

urlpatterns = [
    url(r'^$', views.index, name="dashboard" ),
    url(r'^crear_monedero/$', views.crear_monederos, name="crear_monedero"),
    url(r'^fondear_monedero/(?P<pk>\d+)/$', views.fondear_monederos, name="fondear_monedero"),
]