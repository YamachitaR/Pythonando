from dal import PessoaDal
from model import Pessoa

class PessoaController:
    @classmethod
    def cadastrar(cls, nome, idade, cpf):
        if (len(nome) >  1 and  (int(idade) > 0  and int(idade) < 120)):

            # eh usado try geralmente quando estamo lidando com banco de dado
            # return True para saber se ocorreu tudo bem 
        
            try:
                PessoaDal.salvar(str(Pessoa(nome, idade, cpf)))
                
                return True
            except:
                return False
        else:
            return False 

    @classmethod
    def mostrarPessoa(cls):
        pessoa = PessoaDal.ler()
        if len(pessoa) == 1:
            print("não tem elemento cadastrado")
        else:
            for i in pessoa:
                print(i)