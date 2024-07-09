# Sistema de Gerenciamento de Condomínio

Este projeto é um sistema de gerenciamento de condomínio em Python, que permite gerenciar torres e apartamentos, incluindo a alocação de vagas de garagem e uma fila de espera para apartamentos que aguardam uma vaga. Este trabalho foi desenvolvido para a cadeira de Algoritmos e Estruturas de Dados I do curso de Análise e Desenvolvimento de Sistemas da UniSenac com o Professor Adalto Selau.

## Funcionalidades

- **Cadastrar Apartamento:** Permite o cadastro de apartamentos em torres específicas. Se houver vagas de garagem disponíveis, o apartamento é adicionado a uma lista encadeada ordenada pelo número da vaga. Caso contrário, o apartamento é adicionado a uma fila de espera.
- **Imprimir Apartamentos com Vaga:** Exibe a lista de apartamentos que possuem vaga de garagem.
- **Imprimir Apartamentos sem Vaga:** Exibe a fila de espera dos apartamentos que aguardam uma vaga de garagem.
- **Liberar Vaga:** Libera uma vaga específica de um apartamento, movendo o apartamento para o final da fila de espera e alocando a vaga para o primeiro apartamento na fila.

## Estrutura do Projeto

O projeto é dividido em quatro principais componentes:

- `apartamento.py`: Define a classe `Apartamento`.
- `torre.py`: Define a classe `Torre`.
- `listaEncadeada.py`: Define a classe `ListaEncadeada`, que gerencia a lista de apartamentos com vaga.
- `filaEspera.py`: Define a classe `FilaEspera`, que gerencia a fila de espera dos apartamentos sem vaga.
- `main.py`: O arquivo principal que contém o menu de interação do usuário.

## Como Executar

### Pré-requisitos

- Python 3.x

### Passos para Execução

1. Clone o repositório:

```sh
git clone https://github.com/oThisgo/T1_algoritmos.git
cd T1_algoritmos
