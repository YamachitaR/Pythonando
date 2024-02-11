from Controller import *
from Models import *
from DAO import *


def testeCategoria():
    CategoriaController.cadastrar("Fruta")
    CategoriaController.cadastrar("Lideza")
    CategoriaController.mostrar()
    CategoriaController.excluir("fruta")
    CategoriaController.mostrar()
    CategoriaController.alterar("lideza", "limpeza")
    CategoriaController.mostrar()

def testeProduto():
    a = Produto("alface", 12, 9, Categoria("verdura"))
    ProdutoController.cadastrar(a)
    b = Produto("melao", 12, 9, Categoria("verdura"))
    ProdutoController.cadastrar(b)
    ProdutoController.mostrar()
    ProdutoController.excluir("alface")
    ProdutoController.mostrar()


testeProduto()