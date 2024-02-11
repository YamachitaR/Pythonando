from controller import PessoaController

def opcao():
    try:
        decisao =  int(input( "Digite: \n1 para salva; \n2 para ver a lista salvo, \n3 para sair, \nSua opção:"))
        return decisao
    except:
        return 0

while True:
    decisao = opcao()

    if(decisao == 3):
        break
    elif(decisao == 1):
        nome = input("nome:")
        idade =  input("idade:")
        cpf = input("cpf:")

        if PessoaController.cadastrar(nome, idade, cpf):
            print("Cadastado com sucesso!")
        else:
            print("Falha ao cadastrar!")

    elif(decisao == 2):
        PessoaController.mostrarPessoa()
    else:
        print("Comando invalido!")