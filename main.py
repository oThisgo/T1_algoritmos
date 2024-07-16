from apartamento import Apartamento
from torre import Torre
from filaEspera import FilaEspera
from listaEncadeada import ListaEncadeada

lista = ListaEncadeada()
fila = FilaEspera()
torre1 = Torre("Torre 1", "Rua Treze de Maio, 459")
torre2 = Torre("Torre 2", "Rua Anápio Gomes, 1668")
torre3 = Torre("Torre 3", "Rua Carlos Linck, 635")
torre4 = Torre("Torre 4", "Av. Dorival Candido Luz de Oliveira, 157")

def novo_apto():
    num = input("Digite o número do apartamento: ")
    print('\n')
    torre1.imprimir()
    torre2.imprimir()
    torre3.imprimir()
    torre4.imprimir()
    torre = int(input("\nDigite o número da torre deste apartamento: "))
    
    if torre == 1:
        torre = torre1
    elif torre == 2:
        torre = torre2
    elif torre == 3:
        torre = torre3
    elif torre == 4:
        torre = torre4
    
    apto = Apartamento(num, torre)
    
    if lista.tamanho < 10:
        lista.adicionar(apto)
    else:
        fila.adicionar(apto)

def liberar_vaga():
    vaga = int(input("Digite o número da vaga a ser liberada: "))
    apto_removido = lista.remover(vaga)
    print(f"Apartamento {apto_removido.numero} da {apto_removido.torre.nome} foi removido da vaga {vaga}.")

    if fila.tamanho > 0:
        apto_fila = fila.remover()
        apto_fila.vaga = vaga
        lista.adicionar(apto_fila)
        print(f"Apartamento {apto_fila.numero} da {apto_fila.torre.nome} foi movido para a vaga {vaga}.")
    
    fila.adicionar(apto_removido)
        
def menu():
    while True:
        opcao = int(input("\n ---MENU--- \n0 - EXIT\n1 - Cadastrar Apartamento\n2 - Imprimir Apartamentos com Vaga\n3 - Imprimir Apartamentos sem Vaga\n4 - Liberar Vaga\n\nDigite a opção desejada: "))
            
        if opcao == 0:
            break
              
        elif opcao == 1:
            novo_apto()
            print('\nApartamento adicionado com sucesso!')
                 
        elif opcao == 2:
            lista.imprimir()
              
        elif opcao == 3:
            fila.imprimir()
              
        elif opcao == 4:
            liberar_vaga()
                                        
if __name__ == "__main__":
      menu()