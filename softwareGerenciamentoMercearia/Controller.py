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


    def removerCategoria(self, categoriaRemover):
        x = DaoCategoria.ler()
        cat = list(filter(lambda x: x.categoria == categoriaRemover, x ))

        if len(cat) <= 0:
            print("Categoria nao existe")
        else:
            for i in range(len(x)):
                if x[i].categoria == categoriaRemover:
                    del x[i]
                    break

            with open('categoria.txt', 'w') as arq:
                for i in x:
                    arq.writelines(i.categoria)
                    arq.writelines('\n')
            print("Categoria removido com sucesso")

    def alterarCategoria(self, categoriaAlterar, categoriaAlterada):
        x = DaoCategoria.ler()

        cat = list(filter(lambda x: x.categoria == categoriaAlterar, x))

        if len(cat) > 0 :
            cat1 =  list(filter(lambda x: x.categoria == categoriaAlterada, x))
            if len (cat1) == 0:
                x = list(map(lambda x: Categoria(categoriaAlterada) if (x.categoria ==categoriaAlterar) else (x), x))
                with open('categoria.txt', 'w') as arq:
                    for i in x:
                        arq.writelines(i.categoria)
                        arq.writelines('\n')

                print("Categoria alterado com sucesso")
            else:
                print("A categoria que você desja mudar ja existe")
        else: 
            print("A categoria que voce deseja mudar nao existe")

    def mostrarCategoria(self):
        categorias = DaoCategoria.ler()
        if len(categorias) == 0:
            print("não tem elemento cadastrado")
        else:
            for i in categorias:
                print(f'Categoria: {i.categoria}')



a = ControllerCategoria()

a.mostrarCategoria()
