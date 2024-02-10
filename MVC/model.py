class Pessoa:
    def __init__(self, nome, idade, cpf):
        self.nome = nome
        self.idade = idade 
        self.cpf = cpf

    def __str__(self):
        return f"{self.nome}|{self.idade}|{self.cpf}"