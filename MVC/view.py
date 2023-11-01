from controller import PessoaController

while True:
    deicsao =  int(input( "digitte 1 para salva, 3 para sair: "))

    if(deicsao == 3):
        break
    if(deicsao == 1):
        nome = input("nome")
        idade =  input("idade")
        cpf = input("cpf")

        if PessoaController.cadastrar(nome, idade, cpf):
            print("cadastado com sucesso")
        else:
            print("falha ao cadastrar")


