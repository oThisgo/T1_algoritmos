from filaEspera import FilaEspera

class ListaEncadeada:
    def __init__(self):
        self.topo = None
        self.tamanho = 0
        
    def adicionar(self, apartamento):
        if self.tamanho < 10:
            if self.topo:
                topo = self.topo
                while topo.proximo:
                    topo = topo.proximo
                topo.proximo = apartamento
            else:
                self.topo = apartamento
            self.tamanho += 1
        else:
            pass
        
    def imprimir(self):
        atual = self.topo
        if atual is None:
            print("A lista está vazia.")
        else:
            print("Apartamentos com Vaga:")
            while atual:
                print(f"Apartamento {atual.numero} - {atual.torre.nome}, Vaga {atual.vaga}")
                atual = atual.proximo
            