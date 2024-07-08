class Torre:
    def __init__(self, nome, endereco):
        self.id = 0
        self.nome = nome
        self.endereco = endereco
        
    def imprimir(self):
        print(f"Nome: {self.nome}, Endereço: {self.endereco}")