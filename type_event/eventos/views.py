from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import Evento
from django.urls import reverse
from django.contrib import messages
from django.contrib.messages import constants

# esse @login_required serve para acessa a pagina somente se tiver logado
@login_required
def novo_evento (request):
    if (request.method == "GET"):
        return render(request, 'novo_evento.html')
    elif request.method == "POST":

        #pegando os valores da tabela
        nome = request.POST.get('nome')
        descricao = request.POST.get('descricao')
        data_inicio = request.POST.get('data_inicio')
        data_termino = request.POST.get('data_termino')
        carga_horaria = request.POST.get('carga_horaria')

        cor_principal = request.POST.get('cor_principal')
        cor_secundaria = request.POST.get('cor_secundaria')
        cor_fundo = request.POST.get('cor_fundo')
        
        logo = request.FILES.get('logo')
        
        #seria passando na variavelpara que possamos gravar depois
        evento = Evento(
            criador=request.user,
            nome=nome,
            descricao=descricao,
            data_inicio=data_inicio,
            data_termino=data_termino,
            carga_horaria=carga_horaria,
            cor_principal=cor_principal,
            cor_secundaria=cor_secundaria,
            cor_fundo=cor_fundo,
            logo=logo,
        )

        # salvando no banco de dados
        evento.save()
        
        messages.add_message(request, constants.SUCCESS, 'Evento cadastrado com sucesso')
        return redirect(reverse('novo_evento'))