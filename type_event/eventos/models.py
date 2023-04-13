from django.db import models
from django.contrib.auth.models import User


# aqui vai ser o Banco de Dados
# Acredito que vamos fazer manulmente pois pela complexidade do dado

class Evento(models.Model):
     # Seria para sabe qual usuario criou o evento 
     # nesse caso o Bando de Dado é do tipo um para n, ou seja um usuario pode criar varios evento
     # mas o evento não pode ter varios usuario 
    criador = models.ForeignKey(User, on_delete=models.DO_NOTHING)


     # Serve para prencher com caracteres.  
     # Nesse caso recebe 200 caracteres no maximo
    nome = models.CharField(max_length= 200)
    
    # Texto 
    descricao = models.TextField() 

    data_inicio = models.DateField()
    data_termino = models.DateField()

    carga_horaria = models.IntegerField()

    # Recebe imagem e salva na pasta logos
    logo = models.ImageField(upload_to="logos")

    #Paleta de cores
    #parece que vai ser em hexadecimal
    cor_principal =models.CharField(max_length=7)
    cor_secundaria =  models.CharField(max_length=7)
    cor_fundo = models.CharField(max_length=7)

    def __str__(self) -> str:
        return self.nome

    #depois de fazer tudo isso vamos fazer
    # python3 manage.py makemigrations
    # para pode criar model eventos (estudar mais sobre)

    # Depois fazer
    # python3 manage.py migrate


