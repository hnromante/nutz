from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url
from cuentas import views

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^$', views.home),
    url(r'^cuentas/', include('cuentas.urls')),
    url(r'^evaluacion-nutricional/', include('evaluacionNutricional.urls')),
    url(r'^params-bioquimicos/', include('paramsBioquimicos.urls')),
]              
