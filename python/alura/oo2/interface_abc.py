from collections.abc import Sized

class MinhaListatem(Sized):
    def __init__(self, descrisao, items):
        self.descrisao = descrisao
        self.items = items

    def __str__(self):
        return self.descrisao

    # To fix it

    def __len__(self):
        return len(self.items)

lista = MinhaListatem("Objetos", [1,2,3])
print(len(lista))
print(lista)