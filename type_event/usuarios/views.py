from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.messages import constants
from django.http import HttpResponse


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
    if request.method == "GET":
        return render(request, 'login.html')