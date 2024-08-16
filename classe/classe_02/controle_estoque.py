import os
from dataclasses import dataclass

os.system('cls')

@dataclass
class Produto:
    # Definindo com "dataclass" o tipo de cada atributo da classe
    nome: str
    preco: float
    quantidade: int
    
    def adicionar_estoque(self):
        # os.system('cls')
        print('ATUALIZAR QUANTIDADE EM ESTOQUE\n')
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
        print('ATUALIZAÇÃO DE PREÇO\n')
        try:
            print(f'Preço Atual: R${self.preco:.2f}')
            novo_preco = float(input(f'Novo Preço: '))
            self.preco = novo_preco
            print(f'\nNome do Produto: {self.nome}\nPreço Atualizado: R${self.preco:.2f}')
        except:
            print('Não foi possivel alterar o preço, verifique a quantidade informada!')

    def mostrar_informacoes(self):
        print(f'''
            INFORMAÇÕES DO PRODUTO\n
        Nome do Produto: {self.nome}
        Preço: {self.preco:.2f}
        Quantidade em Estoque: {self.quantidade}
        ''')
    

# produto1 = Produto('Camisa do Bayern',250,50)
# produto1.adicionar_estoque()
# produto1.remover_estoque()
# produto1.atualizar_preco()
# produto1.mostrar_informacoes()

# produto2 = Produto('Camisa do Barcelona',280,150)
# produto2.adicionar_estoque()
# produto2.remover_estoque()
# produto2.atualizar_preco()
# produto2.mostrar_informacoes()

# produto3 = Produto('Camisa do Real Madrid',270,100)
# produto3.adicionar_estoque()
# produto3.remover_estoque()
# produto3.atualizar_preco()
# produto3.mostrar_informacoes()

produto4 = Produto('Camisa Teste Estoque Insuficiente',180,0)
produto4.adicionar_estoque()
produto4.remover_estoque()
produto4.atualizar_preco()
produto4.mostrar_informacoes()




