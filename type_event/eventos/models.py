from django.db import models
from django.contrib.auth.models import User

# Estamos criando o nosso banco de dados manual, acredito seja por causa da complexibilidade

class Evento(models.Model):
    # queremos que nosso Dados seja um para n, 
    #ou seja, um usuario consegue fazer varios eventos 
    criador = models.ForeignKey(User, on_delete=models.DO_NOTHING)

    #todo que estao com Charfield estão pegando os dados
    nome = models.CharField(max_length=200) # quantidade maxima de caracter 200
    descricao = models.TextField()
    data_inicio = models.DateField() # pegando o valor tipo data 
    data_termino = models.DateField()
    carga_horaria = models.IntegerField()
    logo = models.FileField(upload_to="logos") # pegando o tipo imagem, salvando na pasta logos

    # A relaçao vai se de muitos para muitos, ou seja,
    # um participantes pode participar de varios eventos
    # assim como um evento pode ter varios participantes
    participantes = models.ManyToManyField(User, related_name="evento_participante", null=True, blank=True)

    #paleta de cores
    # as vores estao em hexadecimal 
    cor_principal = models.CharField(max_length=7)
    cor_secundaria = models.CharField(max_length=7)
    cor_fundo = models.CharField(max_length=7)
    
    # tem que fazer isso para o nome ficar ceto para aparecer
    def __str__(self):
        return self.nome
    
    # Agora que terminamos o django  vai facilitar fazendo as paradas tb para atualizar
    # python3 manage.py makemigrations
    # python3 manage.py migrate
    # Os dois comando de cima serve para criar ou atualizar o banco de dados 


# Criar banco de dados para o certificado
class Certificado(models.Model):
    certificado = models.ImageField(upload_to="certificados")  # certificado vai ser salvo
    participante = models.ForeignKey(User, on_delete=models.DO_NOTHING) # relaçao do dado, um para n, usuario para varios eventos
    evento = models.ForeignKey(Evento, on_delete=models.DO_NOTHING) # analogo, so que um evento para varios usuarios