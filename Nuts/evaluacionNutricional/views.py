from django.shortcuts import render


def evaluacion_nutricional(request):
    return render(request, template_name='evaluacion_nutricional.html')

def ficha_paciente(request):
    return render(request, template_name='ficha_paciente.html')
