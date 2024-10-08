from Models import *

# Entrar e Saida como objeto 

class DAO:
    @classmethod
    def tipoFile(clc, objeto):
        file = ""
        if  isinstance(objeto, Categoria):
            file = "categoria.txt"
        elif isinstance(objeto, Produto):
            file = "Produto.txt"
        return file 
    
    @classmethod
    def salvar(clc, objeto):
        file = tipoFile(objeto):
        with open(file, 'a') as arq:
            arq.writelines(str(objeto))
            arq.writelines('\n')
    
    @classmethod
    def ler(cls, objeto):
        file = tipoFile(objeto):
        with open(file, 'r') as arq:
            cls.dados = arq.readlines()
        
        cls.dados = list(map(lambda x: x.replace('\n', ''), cls.dados))
        cls.dados = list(map(lambda x: x.split('|'), cls.dados))
        
        lista = []
        for i in cls.dados:
            if isinstance(objeto, Categoria):
                lista.append(Categoria(i))
            elif isinstance(objeto, Produto):
                lista.append(Produto(i[0], i[1], i[2], Categoria(i[3])))
        return lista
    



class CategoriaDao:
    @classmethod
    def salvar(clc, Categoria):
        with open("categoria.txt", 'a') as arq:
            arq.writelines(str(Categoria))
            arq.writelines('\n')
    
    @classmethod
    def ler(cls):
        with open('categoria.txt', 'r') as arq:
            cls.categoria = arq.readlines()
        
        cls.categoria = list(map(lambda x: x.replace('\n', ''), cls.categoria))
        lista = []
        for i in cls.categoria:
            lista.append(Categoria(i))
        return lista
    
    @classmethod
    def regravar(cls, listaCategoria):
        with open("categoria.txt", 'w') as arq:
            for i in listaCategoria:
                arq.writelines(str(i))
                arq.writelines('\n')


class ProdutoDao:
    @classmethod
    def salvar(clc, Produto):
        with open("produto.txt", 'a') as arq:
            arq.writelines(str(Produto))
            arq.writelines('\n')
    @classmethod
    def ler(cls):
        with open('produto.txt', 'r') as arq:
            cls.dados = arq.readlines()
        
        cls.dados = list(map(lambda x: x.replace('\n', ''), cls.dados))
        cls.dados = list(map(lambda x: x.split('|'), cls.dados))

        lista = []
        for i in cls.dados:
            lista.append(Produto(i[0], i[1], i[2], Categoria(i[3])))
        return lista
    
    @classmethod
    def regravar(cls, dados):
        with open("produto.txt", 'w') as arq:
            for i in dados:
                arq.writelines(str(i))
                arq.writelines('\n')