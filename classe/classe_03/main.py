import random
import os
from biblioteca import Biblioteca
from livro import Livro
from cliente import Cliente
from validate_docbr import CPF
import re


def limpa_terminal():
    os.system('cls')

def mensagem_erro(msg_erro):
    print(msg_erro)

def valida_nome_cliente(nome_cliente):
    if not all(c.isalpha() or c.isspace() for c in nome_cliente) or len(nome_cliente) < 5:
        mensagem_erro('O nome só pode conter letras.')
        novo_nome = input('Nome do cliente "Apenas LETRAS e mais de 4 Caracteres.": ').strip()
        return valida_nome_cliente(novo_nome)

    print('\nNome do Cliente Valido!')
    return nome_cliente

def valida_cpf_cliente(cpf_cliente):
    validador = CPF()
    if not validador.validate(cpf_cliente):
        print(f'CPF: {cpf_cliente} é invalido!')
        novo_cpf = input('Informe um CPF valido: ')
        return valida_cpf_cliente(novo_cpf)

    print('\nCPF Valido!')
    return cpf_cliente

def valida_email_cliente(email_cliente):
    email_regex = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    if re.match(email_regex, email_cliente.strip(' ')) == None:
        print(f'O email {email_cliente} fornecido é invalido!')
        novo_email = input('Informe um endereço de email valido: ')
        return valida_email_cliente(novo_email)

    print('\nEmail Valido!')
    return email_cliente

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
    print('CADASTRO DE LIVRO')


def cadastrar_cliente():
    print('Cadastro de Cliente')
    nome_cliente = input('Nome do Cliente: ').strip()
    valida_nome_cliente(nome_cliente)
    cpf_cliente = input('CPF do Cliente: ').strip()
    valida_cpf_cliente(cpf_cliente)
    email_cliente = input('Email do Cliente: ').strip()
    valida_email_cliente(email_cliente)
    
    cliente = Cliente(nome_cliente, cpf_cliente, email_cliente)
    
    print(Biblioteca.verifica_dados_duplicados_clientes(cliente))
    Biblioteca.adiciona_cliente_ao_sistema(cliente)
    print(Biblioteca.exibe_clientes())
    
    return menu_principal()

def exibir_biblioteca():
    print('LIVROS NO SISTEMA DA BIBLIOTECA!')
    print(Biblioteca.exibe_biblioteca())
    input('Digite alguma coisa para voltar ao menu: ')
    return menu_principal()    

def exibir_clientes():
    limpa_terminal()
    print('\nCLIENTES CADASTRADOS NO SISTEMA!')
    print(Biblioteca.exibe_clientes())
    input('Digite alguma coisa para voltar ao menu: ')
    return menu_principal()

def sair():
    print('Obrigado pela visita :)')

def main():
    menu_principal()

if __name__ == '__main__':
    main()
