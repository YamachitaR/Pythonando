from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import Evento, Certificado
from django.urls import reverse
from django.contrib import messages
from django.contrib.messages import constants
import csv
from secrets import token_urlsafe
import os
from django.conf import settings
from PIL import Image, ImageDraw, ImageFont
from io import BytesIO  
from django.core.files.uploadedfile import InMemoryUploadedFile

import sys

# esse @login_required serve para acessa a pagina somente se tiver logado
@login_required
def novo_evento(request):
    if request.method == "GET":
        return render(request, 'novo_evento.html')
    elif request.method == "POST":
        # Pegando os dados
        nome = request.POST.get('nome')
        descricao = request.POST.get('descricao')
        data_inicio = request.POST.get('data_inicio')
        data_termino = request.POST.get('data_termino')
        carga_horaria = request.POST.get('carga_horaria')
        cor_principal = request.POST.get('cor_principal')
        cor_secundaria = request.POST.get('cor_secundaria')
        cor_fundo = request.POST.get('cor_fundo')
        logo = request.FILES.get('logo')
        
        # Preparando para salva no Banco de Dados
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
    
        # salvando 
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


# vai direcionar para pagina de certificado evento
def certificados_evento(request, id):
    evento = get_object_or_404(Evento, id=id)
    if not evento.criador == request.user:
        raise Http404('Esse evento não é seu')
    if request.method == "GET":
        # quantidade de certificado = (total de participante) - (certificado ja gerado)
        qtd_certificados = evento.participantes.all().count() - Certificado.objects.filter(evento=evento).count()
        return render(request, 'certificados_evento.html', {'evento': evento, 'qtd_certificados': qtd_certificados})
    



# como nome ja diz vai ser para gerar o certificado 
def gerar_certificado(request, id):
    # essa 3 linhas abaixo que repete varias vezes
    # serve para garantir quem esta acessando é a pessoa que fez  o evento
    evento = get_object_or_404(Evento, id=id)
    if not evento.criador == request.user:
        raise Http404('Esse evento não é seu')

    # estamos pegando o path do template e da fonte
    path_template = os.path.join(settings.BASE_DIR, 'templates/static/evento/img/template_certificado.png')
    path_fonte = os.path.join(settings.BASE_DIR, 'templates/static/fontes/arimo.ttf')
   
    # gerar certificado para cada participante 
    for participante in evento.participantes.all():
        # Desafio: Validar se já existe certificado desse participante para esse evento
        
        # abrir imagem
        img = Image.open(path_template)
        
        #acho que nao precisa
        #path_template = os.path.join(settings.BASE_DIR, 'templates/static/evento/img/template_certificado.png')
        
        # abrindo imagem no sentindo para modificar
        draw = ImageDraw.Draw(img)
        
        # Fonte nome
        fonte_nome = ImageFont.truetype(path_fonte, 60)
        # Fonte da descrição, esse numero é o tamanho 
        fonte_info = ImageFont.truetype(path_fonte, 30)
        
        # dra.text( posicao, o que quer escrito, fonte, cor) -> para escrever
        # escrevendo nome do particpante, 
        draw.text((230, 651), f"{participante.username}", font=fonte_nome, fill=(0, 0, 0))
        draw.text((761, 782), f"{evento.nome}", font=fonte_info, fill=(0, 0, 0)) # nome do evento 
        draw.text((816, 849), f"{evento.carga_horaria} horas", font=fonte_info, fill=(0, 0, 0)) # carga horaria
        
        # salvando em uma variavel, nao é possivel salvar direto
        output = BytesIO()
        img.save(output, format="PNG", quality=100)
        output.seek(0) # seria tipo para voltar no começo do arquivo

        # preparando o arquivo para ser salvo
        img_final = InMemoryUploadedFile(output,
                                        'ImageField',
                                        f'{token_urlsafe(8)}.png',
                                        'image/jpeg',
                                        sys.getsizeof(output),
                                        None)
        certificado_gerado = Certificado(
            certificado=img_final,
            participante=participante,
            evento=evento,
        )
        #salvando
        certificado_gerado.save()
    
    messages.add_message(request, constants.SUCCESS, 'Certificados gerados')
    return redirect(reverse('certificados_evento', kwargs={'id': evento.id}))