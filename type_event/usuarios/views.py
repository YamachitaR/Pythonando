from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.messages import constants
from django.http import HttpResponse
from django.contrib import auth

def cadastro(request):
    if request.method == "GET":
        return render(request, 'cadastro.html')
    elif request.method == "POST":

        # vai pegar os dados que esta la no cadasro 
        username = request.POST.get('username')
        email = request.POST.get('email')
        senha = request.POST.get('senha')
        confirmar_senha = request.POST.get('confirmar_senha')

        # verifica a senha, caso não for igual voltar no cadastro 
        if not (senha == confirmar_senha):
            messages.add_message(request, constants.ERROR, 'A senha não são as mesma') #messagem de erro    
            return redirect(reverse('cadastro'))
        
        #Lição de casa:  fazer validação de senha forte
      
        # Seria tipo de filtro para depois no verica se usuario ja existe 
        user = User.objects.filter(username=username)
        
        if user.exists(): # verifica se usuario ja existe, caso sim volta na pagina de casdastro
            messages.add_message(request, constants.ERROR, 'Usuario já existe')
            return redirect(reverse('cadastro'))   
        
        # Para cadastrra no banco de dados
        user = User.objects.create_user(username=username, email=email, password=senha)
  #      user.save()
   #     return redirect(reverse('login'))
        messages.add_message(request, constants.SUCCESS, 'Cadastro confirmado!')
        return redirect(reverse('login'))  
    

# Funcao relacionado a login
def login(request):
    if request.method == "GET": #antes de enviar
        return render(request, 'login.html')
    elif request.method == "POST": # depois enviado 

        # pegando variavel login e senha
        username = request.POST.get('username')
        senha = request.POST.get('senha')

        # verificando autenticação 
        user = auth.authenticate(username=username, password=senha)

        # se não der certo permanece na pagina e mostra mensagem de erro
        if not user:
            messages.add_message(request, constants.ERROR, 'Username ou senha inválidos')
            return redirect(reverse('login'))
        
        #autenticado into na pagina de evento 
        auth.login(request, user)
        return redirect('/eventos/novo_evento/')
