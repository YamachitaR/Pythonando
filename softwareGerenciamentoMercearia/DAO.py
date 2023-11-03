from Models import *

class DaoCategoria:
    @classmethod
    def salvar(clc, categoria):
        with open("categoria.txt", 'a') as arq:
            arq.writelines(categoria)
            arq.writelines('\n')
    
    @classmethod 
    def ler (cls): 
        with open('categoria.txt', 'r')  as arq:
            cls.categoria = arq.readlines()
        
        # Estamos retirando barra n
        cls.categoria = list(map(lambda x: x.replace('\n', ''), cls.categoria))

        cat = []
        for i in cls.categoria:
            cat.append(Categoria(i))

        return Categoria


class DaoVenda:
    @classmethod
    def salvar(cls, venda: Venda):
        with open ('venda.txt', 'a') as arq:
            arq.writelines(venda.itensVendido.nome + "|" + venda.itensVendido.preco + "|" + venda.itensVendido.categoria
                           + "|" + venda.vendedor + "|" + venda.comprador + "|" + str(venda.quantidadeVendida) + "|" + venda.data)
            
            arq.writelines('\n')

    @classmethod
    def ler(cls):
        with open ('venda.txt', 'r') as arq:
            cls.venda = arq.readlines()
        
        cls.venda = list(map(lambda x: x.replace('\n', ''), cls.venda))
        cls.venda = list(map(lambda x: x.split('|'), cls.venda))

        vend = []
        for i in cls.venda:
            vend.append(Venda(Produtos(i[0], i[1], i[2]), i[3], i[4], i[5], i[6]))
        return(vend)



class DaoEstoque:
    @classmethod
    def salvar (cls, produto:Produtos,  quantidade):
        with open('estoque.txt', 'a') as arq:
            arq.writelines(produto.name + "|" + produto.preco + "|" + produto.categoria +  "|" + str(quantidade))
            arq.writelines('\n')

    @classmethod
    def ler(cls):
        with open('estoque.txt', 'r') as arq:
            cls.estoque = arq.readlines()
        
        cls.estoque = list(map(lambda x: x.replace('\n', ''), cls.estoque))
        cls.estoque = list(map(lambda x: x.split('|'), cls.estoque))

        est = []
        if len(cls.estoque) > 0:
            for i in cls.estoque:
                est.append(Estoque(Produtos(i[0], i[1], i[2], i[3])))
        
        return est

class DaoFonecedor:
    @classmethod
    def salvar(cls, fonecedor:Fonecedor):
        with open('fornecedores.txt', 'a') as arq:
            arq.writelines(fonecedor.nome + "|" + fonecedor.cnpj + "|" + fonecedor.telefone + "|" + fonecedor.categoria)
            arq.writelines('\n')


    @classmethod
    def ler(cls):
        with open('fonecedores.txt', 'r') as arq:
            cls.fornecedores = arq.readlines()

        cls.fornecedores = list(map(lambda x: x.replace('\n', ''), cls.fornecedores ))
        cls.fornecedores = list(map(lambda x: x.split('|'), cls.fornecedores ))

        forn = []
        for i in cls.fornecedores:
            forn.append(Fonecedor(i[0], i[1], i[2], i[3]))
        
        return forn
    
    # Parei na dao fucionario 
