import os

os.system('cls')
class Produto:
    produtos = []

    def __init__(self, nome: str, preco: float, quantidade: int):
        self.nome = nome
        self.preco = preco
        self.quantidade = quantidade

    def adicionar_estoque(self,item):
        if isinstance(item,Produto):
            self.produtos.append(item)

    def adicionar_qtd(self):
        # os.system('cls')
        print('*'*50)
        print('ATUALIZAR QUANTIDADE EM ESTOQUE')
        print(f'''
            Nome do Produto: {self.nome}
            Qtd. em Estoque: {self.quantidade}    
''')
        try:
            add_quantidade = int(input('Quantidade para adicionar ao estoque: '))
            if add_quantidade <= 0:
                print('Não é possivel adicionar um valor negativo ou igual a zero ao estoque!')
            else:
                self.quantidade = self.quantidade + add_quantidade
                print(f'''
                      Informações do Produto\n
            Nome do Produto: {self.nome} | Qtd. Estoque: {self.quantidade} | Preço R$:{self.preco:.2f}''')
        except:
            print('Não foi possível alterar estoque, verifique a quantidade informada!')
            

    def remover_estoque(self):
        # os.system('cls')
        print('*'*50)
        print('REMOVER DO ESTOQUE')
        if self.quantidade >= 1:
            try:
                print(f'\nEstoque Atual: {self.quantidade}')
                remov_quantidade = int(input('Quantidade para remover do estoque: '))
                if remov_quantidade > self.quantidade:
                    print(f'\nNão foi possivel realizar a operação!\nQuantidade informada ({remov_quantidade}) é maior que a quantidade em estoque ({self.quantidade})')
                elif remov_quantidade <= 0:
                    print('\nO valor não pode ser negativo ou igual a zero!') 
                else:
                    self.quantidade = self.quantidade - remov_quantidade
                    print(f'\nNome do Produto: {self.nome}\nQtd. Estoque Atualizada: {self.quantidade}')
            except:
                print('\nA quantidade informada é invalida!')
        else:
            print('O estoque atual é negativo ou igual a zero, verificar!')
            print(f'Produto: {self.nome} | Estoque Atual: {self.quantidade}')

    def atualizar_preco(self):
        # os.system('cls')
        print('*'*50)
        print('ATUALIZAÇÃO DE PREÇO')
        try:
            print(f'Preço Atual: R${self.preco:.2f}')
            novo_preco = float(input(f'Novo Preço: '))
            self.preco = novo_preco
            print(f'\nNome do Produto: {self.nome}\nPreço Atualizado: R${self.preco:.2f}')
        except:
            print('Não foi possivel alterar o preço, verifique a quantidade informada!')

    def exibe_produtos(self):
        print('Nosso Catalogo')

        for i, item in enumerate(self.produtos):
            print(f'Nome do Produto: {item.nome} | Qtd. Estoque: {item.quantidade} | Preço: {item.preco}')


    def __str__(self):
        return (f'''
            INFORMAÇÕES DO PRODUTO\n
        Nome do Produto: {self.nome}
        Preço: {self.preco:.2f}
        Quantidade em Estoque: {self.quantidade}
        ''')

p1 = Produto('Camisa do Bayern',250,50)
p2 = Produto('Camisa do Barcelona',280,150)
p3 = Produto('Camisa do Real Madrid',270,100)
p4 = Produto('Camisa Teste Estoque Insuficiente',180,0)


p1.adicionar_estoque(p1)
p2.adicionar_estoque(p2)
p3.adicionar_estoque(p3)
p4.adicionar_estoque(p4)

p1.exibe_produtos()

