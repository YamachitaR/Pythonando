from model import Pessoa

class PessoaDal:
    @classmethod
    def salvar(cls, pessoa):
        with open('pessoa.txt', 'w') as arq:
            arq.write(pessoa.nome + " " + str(pessoa.idade) + " " + str(pessoa.cpf))
    
    #não esta finalizado mas eh para ter uma idea com trabalhar 
    @classmethod
    def ler(self):
        nome = "Caio"
        idade = 21
        cpf = 1231232
        return(Pessoa(nome, idade, cpf))
    
