from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth.models import User
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
            return redirect('/usuarios/cadastro')
#           return redirect(reverse('cadastro'))
        
        return HttpResponse ('teste')
        # Vamos criar uma variavel para podemo enviar
 #       user = User.objects.filter(username=username)

#        if user.exists():
#            return redirect(reverse('cadastro'))   
        
 #       user = User.objects.create_user(username=username, email=email, password=senha)
  #      user.save()
   #     return redirect(reverse('login'))