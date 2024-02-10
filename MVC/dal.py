from model import Pessoa

class PessoaDal:
    @classmethod
    def salvar(cls, pessoa):
        with open('pessoa.txt', 'a') as arq:
            arq.writelines(pessoa)
            arq.writelines('\n')
    
    @classmethod
    def ler(cls):
        with open('pessoa.txt', 'r') as arq:
            cls.pessoa = arq.readlines()
        
        cls.pessoa = list(map(lambda x: x.replace('\n', ''), cls.pessoa))
        cls.pessoa = list(map(lambda x: x.split('|'), cls.pessoa))

        lista = []
        for i in cls.pessoa:
            lista.append(str(i))

        return lista
    
