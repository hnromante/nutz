from django.shortcuts import render

def params_bioquimicos(request):
    return render(request, template_name='parametros_bioquimicos.html')