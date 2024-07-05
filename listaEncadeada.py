from apartamento import Apartamento
from filaEspera import FilaEspera

class ListaEncadeada:
    def __init__(self):
        self.topo = None
        self.tamanho = 0
        
    def adicionar(self, item)
        if self.tamanho < 10:
            if self.topo:
                topo = self.topo
                while (topo.proximo):
                    topo = topo.proximo
                topo.proximo = Apartamento(item)
            else:
                self.topo = Apartamento(item)
            self.tamanho += 1
        elif self.tamanho == 10:
            FilaEspera.adicionar(item)
            