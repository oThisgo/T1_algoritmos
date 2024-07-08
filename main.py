from apartamento import Apartamento
from torre import Torre
from listaEncadeada import ListaEncadeada

lista = ListaEncadeada()
torre1 = Torre("Torre 1", "Rua Treze de Maio, 459")
torre2 = Torre("Torre 2", "Rua Anápio Gomes, 1668")
torre3 = Torre("Torre 3", "Rua Carlos Linck, 635")
torre4 = Torre("Torre 4", "Av. Dorival Candido Luz de Oliveira, 157")

def novo_apto():
    num = input("Digite o número do apartamento: ")
    torre = int(input(f"1 - {torre1.imprimir()}\n2 - {torre2.imprimir()}\n3 - {torre3.imprimir()}\n4 - {torre4.imprimir()}\n\nDigite a torre deste apartamento: "))
    
    if torre == 1:
        torre = torre1
    elif torre == 2:
        torre = torre2
    elif torre == 3:
        torre = torre3
    elif torre == 4:
        torre = torre4
    
    apto = Apartamento(num, torre)
    lista.adicionar(apto)

def menu():
    while True:
        opcao = int(input("0 - EXIT\n1 - Cadastrar Apartamento\n2 - Imprimir Apartamentos com Vaga\n3 - Imprimir Apartamentos sem Vaga\n4 - Liberar Vaga\n\nDigite a opção desejada:"))
            
        if opcao == 0:
            break
              
        elif opcao == 1:
            novo_apto()
            print('\nApartamento adicionado com sucesso!\n')
                 
        elif opcao == 2:
            lista.imprimir()
              
        elif opcao == 3:
            pass
              
        elif opcao == 4:
            pass
                                        
if __name__ == "__main__":
      menu()