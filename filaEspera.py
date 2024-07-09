class FilaEspera:
    def __init__(self):
        self.topo = None
        self.tamanho = 0
    
    def adicionar(self, apartamento):
        if self.topo is None:
            self.topo = apartamento
        else:
            atual = self.topo
            while atual.proximo:
                atual = atual.proximo
            atual.proximo = apartamento
        self.tamanho += 1
        
    def remover(self):
        if self.topo is None:
            raise IndexError("A fila está vazia. Não é possível remover nenhum item.")
        
        item_removido = self.topo
        self.topo = self.topo.proximo
        self.tamanho -= 1
        item_removido.proximo = None
        return item_removido
        
    def imprimir(self):
        atual = self.topo
        if atual is None:
            print("\nA fila está vazia.")
        else:
            print("\nApartamentos na Fila de Espera:")
            while atual:
                print(f"Apartamento {atual.numero} - {atual.torre.nome}")
                atual = atual.proximo