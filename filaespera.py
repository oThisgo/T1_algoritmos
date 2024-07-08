class FilaEspera:
    def __init__(self):
        self.topo = None
        self.tamanho = 0
    
    def adicionar(self, item):
            
        item.proximo = self.topo
        self.topo = item
        self.tamanho += 1