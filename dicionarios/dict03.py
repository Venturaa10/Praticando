import os
os.system('cls')
# EXERCICIOS PARA REVISÃO 

# 1 - Definições Simples:
# Crie um dicionário com algumas palavras e suas definições. Peça ao usuário para inserir uma palavra e, em seguida, mostre a definição correspondente. (FEITO)
dicionario = {'Simples' : 'Algo Fácil', 'Pedra' : 'Duro e vem de rocha', 'Planta': 'Verde e leve'}

palavra = input('Digite a palavra: ')
definicao = input(f'Defina a palavra {palavra}: ')

dicionario[palavra] = definicao

print(dicionario)

# 2- Adicionar e Remover Palavras:
# Permita que o usuário adicione novas palavras e suas definições ao dicionário. Depois, permita que ele remova palavras existentes, caso deseje.

# 3 - Pesquisa de Palavras:
# Peça ao usuário para inserir uma palavra. Verifique se a palavra está presente no dicionário e, se estiver, mostre sua definição. Caso contrário, exiba uma mensagem indicando que a palavra não foi encontrada.

# 4 - Listar Todas as Palavras:
# Mostre todas as palavras presentes no dicionário, uma por linha.

# 5 - Contagem de Palavras:
# Conte quantas palavras existem no dicionário e exiba o total para o usuário.
