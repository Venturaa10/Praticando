import random
import os
from biblioteca import Biblioteca
from livro import Livro
from cliente import Cliente

def limpa_terminal():
    os.system('cls')

def menu_principal():
    print('''
            SISTEMA BIBLIOTECA\n
            1 - Cadastrar Livro
            2 - Cadastrar Cliente
            3 - Exibir Biblioteca
            4 - Exibir CLientes
            0 - Sair
                ''')
    try:
        seleciona_opcao = int(input('Número da Opção: '))
    except: 
        limpa_terminal()
        print('Opção Inválida, informe uma das opções exibidas abaixo!')
        return menu_principal()

    if seleciona_opcao == 1:
        cadastrar_livro()
    elif seleciona_opcao == 2:
        cadastrar_cliente()
    elif seleciona_opcao == 3:
        exibir_biblioteca()
    elif seleciona_opcao == 4:
        exibir_clientes()
    elif seleciona_opcao == 0:
        sair()
    else:
        limpa_terminal()
        print('Opção Inválida!')
        return menu_principal()

def cadastrar_livro():
    print('CADASTRO DE CLIENTE')

def cadastrar_cliente():
    print('Cadastro de Cliente')

def exibir_biblioteca():
    print('Exibe Biblioteca')

def exibir_clientes():
    print('Exibe Clientes')

def sair():
    print('Obrigado pela visita :)')

def main():
    menu_principal()

if __name__ == '__main__':
    main()
