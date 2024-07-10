class Torre:
    def __init__(self, nome, endereco):
        self.id = 0
        self.nome = nome
        self.endereco = endereco
        
    def cadastrar(self):
        pass
        
    def imprimir(self):
        print(f"{self.nome}, Endereço: {self.endereco}")