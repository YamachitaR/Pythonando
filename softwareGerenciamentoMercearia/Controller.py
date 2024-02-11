from Models import *
from DAO import *


class CategoriaController:
    @classmethod
    def cadastrar(cls, categoria):
        try:
            if CategoriaController.existe(categoria):
                print("Produto já cadastrado!")
                return False
            else:
                CategoriaDao.salvar(categoria)
                return True
        except:
            return False

    @classmethod 
    def mostrar(cls):
        try:
            dados = CategoriaDao.ler()
            if len(dados) == 0:
                print("Não tem elemento no banco de dados")
            else:
                print("|Banco de Dado Cadastro|")
                for i in dados:
                    print(i.categoria)
        except:
            return False


    @classmethod
    def existe(cls, elemento):
        try:
            dados = CategoriaDao.ler()
            for i in dados:
                if i.categoria.upper() == elemento.upper():
                    return True
            return False
        except:
            return False
        

    @classmethod
    def excluir(cls, elemento):
        if not (CategoriaController.existe(elemento)):
            print("Não existe esse elemento no banco de dados")
            return False
        
        dados = CategoriaDao.ler()
        lista = []
        for i in dados:
            if i.categoria.upper() != elemento.upper():
                lista.append(i)

        CategoriaDao.regravar(lista)
        print("Excluido com Sucesso!")
        return True
    
    @classmethod
    def alterar(cls, velho, novo):
        if not(CategoriaController.existe(velho)):
            print("Não existe esse elemento no banco de dados")
            return False
        if (CategoriaController.existe(novo)):
            print("Já existe essa categoria")
            return False
        
        dados = CategoriaDao.ler()
        lista = []
        for i in dados:
            if i.categoria.upper() == velho.upper():
                lista.append(novo)
            else:
                lista.append(i)

        CategoriaDao.regravar(lista)
        print("Alterado com Sucesso!")
        return True
    




class ProdutoController:
    @classmethod
    def cadastrar(cls, Produto):
        try:
            if ProdutoController.existe(Produto.nome):
                print("Produto já cadastrado!")
                return False
            else:
                ProdutoDao.salvar(Produto)
                print("Produto cadastrado com Sucesso!")
                return True
        except:
            print("Houve falha ao cadastrar")
            return False

    

    @classmethod 
    def mostrar(cls):
        try:
            dados = ProdutoDao.ler()
            if len(dados) == 0:
                print("Não tem elemento no banco de dados")
        
            else:
                print("|Banco de Dado do Produto|")
                for i in dados:
                    print(str(i))
        except:
            return False

    @classmethod
    def existe(cls, elemento):
        
        try:
            
            dados = ProdutoDao.ler()
            for i in dados:
                if i.nome.upper() == elemento.upper():
                    return True
            return False  

        except:
            return False
        


    @classmethod
    def excluir(cls, elemento):
        if not (ProdutoController.existe(elemento)):
            print("Não existe esse elemento no banco de dados")
            return False
        
        dados = ProdutoDao.ler()
        lista = []
        for i in dados:
            if i.nome.upper() != elemento.upper():
                lista.append(i)

        ProdutoDao.regravar(lista)
        print("Excluido com Sucesso!")
        return True
    
    @classmethod
    def alterar(cls, velho, novo):
        if not(ProdutoController.existe(velho.nome)):
            print("Não existe esse elemento no banco de dados")
            return False
        if (ProdutoController.existe(novo.nome)):
            print("Já existe essa categoria")
            return False
        
        dados = ProdutoDao.ler()
        lista = []
        for i in dados:
            if i.nome.upper() == velho.nome.upper():
                lista.append(novo)
            else:
                lista.append(i)

        CategoriaDao.regravar(lista)
        print("Alterado com Sucesso!")
        return True