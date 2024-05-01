import os
os.system('cls')
# Sintaxe Basica: dicionario = {'chave': valor, 'chave2': valor2}

# 1 - Crie um dicionário vazio chamado meu_dicionario e adicione três pares chave-valor a ele, representando nomes de frutas e suas quantidades. (FEITO)
frutas = {}
"""Sintaxe para adicionar chave e valor ao dicionario:
dicionario['Chave'] = valor
"""

frutas['Banana'] = 20
frutas['Pera'] = 30
frutas['Maça'] = 10
print(f'Frutas: {frutas}')
# 2 - A partir do dicionário anterior, adicione uma nova fruta com sua quantidade.(FEITO)

frutas['Morango'] = 50
print(f'Frutas: {frutas}')

# 3 - Escreva um código para verificar se uma determinada fruta está presente no dicionário.(FEITO)
'''
nome_fruta = input('Nome da Fruta: ').capitalize().strip()

if nome_fruta in frutas:
    print(f'A fruta {nome_fruta} está presente no dicionário')
else:
    print(f'A fruta {nome_fruta} não está presente no dicionário')

print()
'''

# 4 - Escreva um programa para imprimir todas as chaves do dicionário.(FEITO)
'''
"""As duas maneiras que consegui"""
print(frutas.keys())
for chave in frutas.keys():
    print(f'Chaves do dicionário Fruta: {chave}')

print()
'''
# 5 - Escreva um código para imprimir todos os valores do dicionário.(FEITO)
'''
"""As duas maneiras que consegui"""
print(frutas.values())
for valor in frutas.values():
    print(valor)
print()
'''
# 6 - Escreva um programa para calcular o total de todas as quantidades de frutas no dicionário.(FEITO)
'''
print(f'Quantidades de unidades de frutas: {sum(frutas.values())}')
'''
# 7 - Escreva um código para encontrar a fruta com a maior quantidade no dicionário. 
# Remova uma fruta do dicionário e imprima o dicionário atualizado.  (FEITO)
# Limpe o dicionário, removendo todos os itens.(Feito)
# Crie um novo dicionário contendo pelo menos três frutas diferentes e suas quantidades e, em seguida, combine esse dicionário com o primeiro dicionário criado.(FEITO)

for fruta in frutas:
    print(fruta)

"""Revisar a explicação da 'key=lambda' 

- frutas.items() retorna uma lista de tuplas contendo cada par chave-valor do dicionário.
- max() é usado para encontrar o par chave-valor com o maior valor no dicionário.
- A chave key=lambda item: item[1] especifica que a comparação deve ser feita com base no segundo elemento de cada tupla, que representa a quantidade da fruta.

maior_qtd[0] retorna a chave da fruta com a maior quantidade.
maior_qtd[1] retorna a quantidade da fruta com a maior quantidade.


"""
maior_qtd = max(frutas.items(), key=lambda item:item[1])
print(f'O(A) {maior_qtd[0]} é a fruta em maior quantidade no estoque, contendo: {maior_qtd[1]} unidades.')
"""
print(f'Removendo fruta: {frutas.popitem()}\n') #Remove o ultimo item adicionado ao dicionario
"""
"""
print(f'Removendo chave especifica: {frutas.pop('Pera')}') #Remove a chave especifica, e retorna o valor dessa chave
print(f'Dicionario atualizado: {frutas}')
print()
"""
"""
frutas2 = {}
frutas2['Abacaxi'] = 27
frutas2['Laranja'] = 17
frutas2['Goiaba'] = 15

frutas.update(frutas2)
print(f'Juntando os dois dicionarios de frutas: {frutas}')


print()
frutas.clear()
if len(frutas) == 0:
    print('Não há frutas!')
else:
    print(frutas)
"""

