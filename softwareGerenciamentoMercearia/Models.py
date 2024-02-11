from datetime import datetime

class Categoria:
    def __init__(self,categoria):
        self.categoria = categoria

    def __str__(self):
        return f"{self.categoria}"
    

class Produto:
    def __init__(self, nome, qtd, preco, categoria:Categoria):
        self.nome =  nome
        self.qtd = qtd
        self.preco = preco
        self.categoria = categoria
    

    def __str__(self):
        return f"{self.nome}|{self.qtd}|{self.preco}|{self.categoria}"