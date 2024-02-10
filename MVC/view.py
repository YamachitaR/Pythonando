from controller import PessoaController

def opcao():
    try:
        decisao =  int(input( "digitte 1 para salva, 2 para ver as pessoas salvo, 3 para sair:"))
        return decisao
    except:
        print("digite numero")
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
            print("cadastado com sucesso")
        else:
            print("falha ao cadastrar")

    elif(decisao == 2):
        PessoaController.mostrarPessoa()
    else:
        print("Comando invalido")