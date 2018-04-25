from django.conf.urls import url
from paramsBioquimicos import views

urlpatterns = [
    url(r'^$', views.params_bioquimicos, name='params-bioquimicos')
    
]
