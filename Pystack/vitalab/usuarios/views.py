from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.messages import constants
from django.contrib import messages
from django.contrib.auth import authenticate, login

# Create your views here.
def cadastro(request):
    if request.method == "GET":
        return render(request, 'cadastro.html')
    else:
        primeiro_nome = request.POST.get('primeiro_nome')
        ultimo_nome = request.POST.get('ultimo_nome')
        username = request.POST.get('username')
        email = request.POST.get('email')
        senha = request.POST.get('senha')
        confirmar_senha = request.POST.get('confirmar_senha')

        if not senha == confirmar_senha:
            messages.add_message(request, constants.ERROR, 'As senhas não são iguais')
            return redirect('/usuarios/cadastro')
        if len(senha) < 6:
            messages.add_message(request, constants.ERROR, 'A senha tem que ter mais de 6 digitos')
            return redirect('/usuarios/cadastro')
        
        try:
            # To do:Username deve ser único!
            # esse User é do proprio do Django que ajudar a validar os dados
            user = User.objects.create_user(
                first_name=primeiro_nome,
                last_name=ultimo_nome,
                username=username,
                email=email,
                password=senha,
                )
            messages.add_message(request, constants.SUCCESS, 'Cadastro com Sucesso!!!!!!!!!!')
        except:
            messages.add_message(request, constants.ERROR, 'Erro ao cadastrar')
            return redirect('/usuarios/cadastro')
        

        return redirect('/usuarios/cadastro')
    

def logar(request):
    if request.method == "GET":
        return render(request, 'login.html')
    else:
        username = request.POST.get('username')
        senha = request.POST.get('senha')

        # verifica se login e senha esta ok
        user = authenticate(username=username, password=senha)

        # Caso tiver ok vai logar 
        if user:
            login(request, user)
            # Acontecerá um erro ao redirecionar por enquanto, resolveremos nos próximos passos
            return HttpResponse("estou logado")
        else:
            messages.add_message(request, constants.ERROR, 'Usuario ou senha inválidos')
            return redirect('/usuarios/login')