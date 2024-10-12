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
        # Verificação inicial para evitar valores negativos
        if preco < 0:
            raise ValueError("Preço não pode ser negativo!")
        if quantidade < 0:
            raise ValueError("Quantidade não pode ser negativa!")
    
        self.nome = nome
        self.preco = preco
        self.quantidade = quantidade

    def adicionar_estoque(self, quantidade): 
        ''' Adiciona uma quantidade fornecida pelo usuario ao estoque'''
        if quantidade <= 0:
            raise ValueError('Valor inválido, a quantidade não pode ser menor ou igual a 0!') 
        else:
            self.quantidade += quantidade

    def remover_estoque(self, quantidade):
        ''' Remove determinada quantidade do estoque, se o estoque for maior que 0'''
        if self.quantidade <= 0:
            raise ValueError('Estoque insuficiente!')
        
        if quantidade > self.quantidade:
            raise ValueError(f'Quantidade fornecida {quantidade} é maior que a quantidade em estoque {self.quantidade}!')
        else:
            self.quantidade -= quantidade

    def atualizar_preco(self, novo_preco):
        ''' Atualiza o preço do produto'''
        if novo_preco < 0:
            raise ValueError('Valor inválido, o preço não pode ser negativo! ')
        else:
            self.preco = novo_preco
            

    def mostrar_informacoes(self):
        return f'Produto: {self.nome} | Quantidade: {self.quantidade} | Preço: {self.preco:.2f}'
        
camisa1 = Produto('Camisa Barcelona', 250, 0)
camisa1.adicionar_estoque(50)
camisa1.remover_estoque(25)
camisa1.atualizar_preco(280)
print(camisa1.mostrar_informacoes())

camisa2 = Produto('Camisa do Manchester City', 200, 75)
camisa2.adicionar_estoque(70)
camisa2.remover_estoque(100)
camisa2.atualizar_preco(230)
print(camisa2.mostrar_informacoes())

camisa3 = Produto('Camisa do Flamengo', 300, 45)
camisa3.adicionar_estoque(90)
camisa3.remover_estoque(65)
camisa3.atualizar_preco(320)
print(camisa3.mostrar_informacoes())


