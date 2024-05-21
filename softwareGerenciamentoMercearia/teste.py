class MinhaClasse:
    pass

class OutraClasse:
    pass

objeto = MinhaClasse()


def identificar(objeto):
    if isinstance(objeto, MinhaClasse):
        print("O objeto pertence à classe MinhaClasse")
    else:
        print("O objeto não pertence à classe MinhaClasse")


identificar(objeto)
identificar(OutraClasse)