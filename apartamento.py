import random

class Apartamento:
    def __init__(self, numero, torre, vaga = None):
        self.id = 0
        self.numero = numero
        self.torre = torre
        self.vaga = vaga if vaga is not None else random.randint(100, 200)
        self.proximo = None
        
    def cadastrar(self):
        pass
        
    def imprimir(self):
        print(f"Apartamento {self.numero} - Torre: {self.torre} - Vaga: {self.vaga}")