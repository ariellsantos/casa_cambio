from django.conf.urls import url
from . import views

app_name = "divisas"

urlpatterns = [
    url(r'^$', views.index, name="dashboard" )
]