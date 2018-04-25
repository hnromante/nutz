from django.conf.urls import url
from evaluacionNutricional import views

urlpatterns = [
    url(r'^$', views.evaluacion_nutricional, name='evaluacion-nutricional'),
    url(r'^ficha-paciente/$', views.ficha_paciente, name='ficha-paciente'),

    
]
