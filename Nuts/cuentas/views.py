from django.shortcuts import render


#VISTAS BASADAS EN FUNCIONS V/S VISTAS BASADAS EN CLASES
def home(request):
    return render(request,'base.html')

def login(request):
    return render(request, template_name='login.html')

def registrar(request):
    return render(request, template_name='registrar.html')