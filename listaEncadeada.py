class ListaEncadeada:
    def __init__(self):
        self.topo = None
        self.tamanho = 0
        
    def adicionar(self, apartamento):
        if self.topo:
            topo = self.topo
            while topo.proximo:
                topo = topo.proximo
            topo.proximo = apartamento
        else:
            self.topo = apartamento
        self.tamanho += 1
        
    def remover(self, vaga):
        if self.topo is None:
            raise IndexError("A lista está vazia.")
        
        if self.topo.vaga == vaga:
            item_removido = self.topo
            self.topo = self.topo.proximo
            self.tamanho -= 1
            return item_removido

        anterior = self.topo
        atual = self.topo.proximo
        while atual is not None:
            if atual.vaga == vaga:
                anterior.proximo = atual.proximo
                self.tamanho -= 1
                return atual
            anterior = atual
            atual = atual.proximo
        
        raise ValueError("Apartamento com a vaga especificada não encontrado.")
    
    def imprimir(self):
        atual = self.topo
        if atual is None:
            print("\nA lista está vazia.")
        else:
            print("\nApartamentos com Vaga:")
            while atual:
                print(f"Apartamento {atual.numero} - {atual.torre.nome}, Vaga {atual.vaga}")
                atual = atual.proximo
            