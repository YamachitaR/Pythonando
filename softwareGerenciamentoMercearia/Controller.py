from Models import Categoria, Estoque, Produtos, Fonecedor, Pessoa, Funcionario, Venda
from DAO import DaoCategoria, DaoEstoque, DaoVenda, DaoFonecedor, DaoPessoa, DaoFuncionario
from datetime import datetime

class ControllerCategoria:
    def cadastraCategoria(self, novaCategoria):
        existe = False
        x = DaoCategoria.ler()
        for i in x:
            if i.categoria == novaCategoria:
                existe = True

        if not existe:
            DaoCategoria.salvar(novaCategoria)
            print('Categoria cadastro com sucesso')

        else:
            print('essa categoria já esta cadastrado')

a = ControllerCategoria()

a.cadastraCategoria('frios')
