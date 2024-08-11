import os
os.system('cls')

'''Objetivo: Gerenciamento de Estoque
Você vai criar um sistema simples para gerenciar o estoque de produtos. O sistema deve permitir as seguintes operações:

Criação de Produtos:

Defina uma classe Produto com os atributos:
nome (string)
preço (float)
quantidade (int)
Métodos da Classe Produto:

adicionar_estoque(quantidade): Adiciona a quantidade especificada ao estoque do produto.
remover_estoque(quantidade): Remove a quantidade especificada do estoque do produto, se houver estoque suficiente.
atualizar_preço(novo_preço): Atualiza o preço do produto.
mostrar_informacoes(): Exibe o nome, preço e quantidade atual do produto.
Funções Adicionais:

Criar Produtos:
Crie pelo menos três produtos com nomes, preços e quantidades diferentes.
Adicionar/Remover Estoque:
Realize operações de adição e remoção de estoque para esses produtos.
Atualizar Preços:
Atualize o preço de pelo menos um dos produtos.
Exibir Status do Estoque:
Mostre as informações (nome, preço e quantidade) de todos os produtos.
O objetivo é implementar e testar essas funcionalidades para gerenciar o estoque de forma eficiente.
'''

class Produto:
    def __init__(self, nome, preco, quantidade):
        self.nome = nome
        self.preco = preco
        self.quantidade = quantidade

    def adicionar_estoque(self, add_quantidade):
        os.system('cls')
        print('Atualizar Quantidade em Estoque')
        self.quantidade = self.quantidade + add_quantidade
        return print(f'Nome do Produto: {self.nome}\nQtd. Estoque Atualizada: {self.quantidade}')


    def remover_estoque(self, remov_quantidade):
        print('Remover do estoque')

        if self.quantidade < 1:
            print(f'Estoque insuficiente do produto {self.nome}! ')
        else:
            print(f'Nome do Produto: {self.nome}\nQtd. Estoque Atualizada: {self.quantidade:.2f}')
            # remov_quantidade = input(int('Quantas unidades deseja remover do estoque? '))
            return 

    def atualizar_preco(self, novo_preco):
        print('ATUALIZAÇÃO DE PREÇO')
        novo_preco = input(int(f'Novo preço do produto {self.nome}: '))
        self.preco = novo_preco

    def mostrar_informacoes(self):
        print(f'''
        Nome do Produto: {self.nome}
        Preço: {self.preco}
        Quantidade em Estoque: {self.quantidade:.2f}
        ''')
    

produto1 = Produto('Camisa do Bayern',250,50)
produto1.adicionar_estoque(25)
produto1.adicionar_estoque(25)
produto1.mostrar_informacoes()




