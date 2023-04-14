from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import Evento
from django.urls import reverse
from django.contrib import messages
from django.contrib.messages import constants
import csv
from secrets import token_urlsafe
import os
from django.conf import settings

# esse @login_required serve para acessa a pagina somente se tiver logado
@login_required
def novo_evento(request):
    if request.method == "GET":
        return render(request, 'novo_evento.html')
    elif request.method == "POST":
        nome = request.POST.get('nome')
        descricao = request.POST.get('descricao')
        data_inicio = request.POST.get('data_inicio')
        data_termino = request.POST.get('data_termino')
        carga_horaria = request.POST.get('carga_horaria')

        cor_principal = request.POST.get('cor_principal')
        cor_secundaria = request.POST.get('cor_secundaria')
        cor_fundo = request.POST.get('cor_fundo')
        
        logo = request.FILES.get('logo')
        
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
    
        evento.save()
        
        messages.add_message(request, constants.SUCCESS, 'Evento cadastrado com sucesso')
        return redirect(reverse('novo_evento'))
    
# @login_required
# pagina do gerencia evento 
def gerenciar_evento(request):
    if request.method == "GET":

        # vai pegar o nome para depois nos filtrar
        nome = request.GET.get('nome')

        #vai pegar so eventos do proprio usuario 
        eventos = Evento.objects.filter(criador=request.user)

        # se o nome contiver algo é pq usuario que que filtre
        if nome:
            eventos = eventos.filter(nome__contains=nome)

            # se fosse somente 
            #eventos = eventos.filter(nome=nome)
            # nome do lado esquedo esta relacionado a tabela e o lado direito da nossa variavel
            # nesse caso usuario tem que digitar exatamente igual para aparecer
            # ao fazer "nome__contains" significa pelo menos tem que conter 

            # Desafio: fazer outros tipos de filtro, por exemplo por data

        # Repare nesse eventos que é um dicionario, vai se importante para imprimir na pagina
        return render(request, 'gerenciar_evento.html', {'eventos': eventos})
    
#@login_required  tirar comentario depois
# vai se aquela pagina de inscerver
def inscrever_evento(request, id):
	
    # esse id sera pagina especifivca do evento
    # caso nao existir a pagina vai aparecer a pagina de erro 404
    # praticamente esta procurando se existe o evento no banco de dados
    evento = get_object_or_404(Evento, id=id)
    if request.method == "GET":
        return render(request, 'inscrever_evento.html', {'evento': evento})
    elif request.method == "POST":
        # Validar se o usuário já é um participante
        evento.participantes.add(request.user)
        evento.save()

        messages.add_message(request, constants.SUCCESS, 'Inscrição com sucesso.')
        return redirect(reverse('inscrever_evento', kwargs={'id': id}))
    

def participantes_evento(request, id):
    evento = get_object_or_404(Evento, id=id)
    # esse if faz com que somente a pessoa que criou o evento tenha acesso
    if not evento.criador == request.user:
        raise Http404('Esse evento não é seu')
    if request.method == "GET":
        participantes = evento.participantes.all()[::3] # aqui eh uma lista so para aparece 3 primeiros
        return render(request, 'participantes_evento.html', {'evento': evento, 'participantes': participantes})
    

def gerar_csv(request, id):
    evento = get_object_or_404(Evento, id=id)
    if not evento.criador == request.user:
        raise Http404('Esse evento não é seu')
    
    # Pegando todos os particiapantes
    participantes = evento.participantes.all() 
    
    # criando nome aleartorio de extensao csv
    token = f'{token_urlsafe(6)}.csv'

    # cocatenando nome da pasta (midia) com o nome gerado
    path = os.path.join(settings.MEDIA_ROOT, token)

    # Abrindo o arquivo
    with open(path, 'w') as arq:
        # escrevendo com delimitado sendo virgula
        writer = csv.writer(arq, delimiter=",")
        for participante in participantes:
            #informacao que queremos grava que sao nome e email
            x = (participante.username, participante.email)
            # gravando
            writer.writerow(x)
    # ennviando o arquivo
    return redirect(f'/media/{token}')