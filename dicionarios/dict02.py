import os
import random
os.system('cls')

# 1- Contagem de Palavras:
# Escreva um programa que recebe uma string como entrada e conta a ocorrência de cada palavra na string. Em seguida, armazene essas contagens em um dicionário onde as chaves são as palavras e os valores são as contagens de ocorrências.

"""Dicionario"""
armazena_palavra = {}

"""Loop para realizar a pergunta e armazenar dentro do dicionario"""
for i in range(0,8):
    palavra = input('Palavra: ').capitalize().strip()
    
    """Se palavra já existir no dicionario, a contagem de ocorrencia acontecera da seguinte forma: 
    A variavel 'ocorrencia' recebe a palavra dentro do dicionario e atualiza o valor através do metodo '.get' que retorna o valor de determinada chave, pois já que o valor é inteiro, eu acrescento + 1 a esse valor e ao mesmo tempo atualizo o valo da chave dentro do dicionario.
    Se não, essa palavra é adionada ao dicionario e com o valor padrão 1, pois é a primeira ocorrencia dessa palavra.
    """
    if palavra in armazena_palavra: 
        ocorrencia = armazena_palavra[palavra] = armazena_palavra.get(palavra) + 1
        print(f'Essa é a {ocorrencia}º ocorrencia da palavra {palavra}')

    else:
        print(f'{palavra} adicionada ao dicionário!\n')
        armazena_palavra[palavra] = 1

print(armazena_palavra)

# 2 - Mesclar Dicionários Únicos:
# Escreva uma função que aceita uma lista de dicionários como entrada e retorna um único dicionário que contém todas as chaves e seus respectivos valores únicos de todos os dicionários de entrada.
 

# 3 - Média de Notas:
# Escreva um programa que pede ao usuário para inserir o número de alunos em uma turma, seus nomes e suas notas (em uma escala de 0 a 10) como entrada. Em seguida, calcule e imprima a média das notas. Armazene os nomes dos alunos como chaves e suas notas como valores em um dicionário.

