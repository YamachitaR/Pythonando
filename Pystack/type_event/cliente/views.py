from django.shortcuts import render
from eventos.models import Certificado

# Create your views here.

def meus_certificados(request):
    # vai trazer todos certificado que a pessoa esta logado 
    certificados = Certificado.objects.filter(participante=request.user)
    return render(request, 'meus_certificados.html', {'certificados': certificados})