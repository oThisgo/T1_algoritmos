import random

class Apartamento:
    def __init__(self, numero, torre):
        self.id = 0
        self.numero = numero
        self.torre = torre
        self.vaga = random.randint(100, 900)
        self.proximo = None
        
    def cadastrar(self):
        pass
        
    def imprimir(self):
        print(f"Apartamento {self.numero} - Torre: {self.torre} - Vaga: {self.vaga}")