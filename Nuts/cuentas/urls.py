from django.conf.urls import url
from cuentas import views

urlpatterns = [
    url(r'^login/$', views.login, name='login'),
    url(r'^registrar/$', views.registrar, name='registrar'),
]
