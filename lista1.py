import os
from math import prod
os.system('cls')

# Faça um Programa que leia um vetor de 5 números inteiros e mostre-os.(FEITO)
'''
lista_numeros = [30,34,56,65,43]
print(lista_numeros)

for numero in lista_numeros:
    print(numero)
'''
# Faça um Programa que leia um vetor de 10 números reais e mostre-os na ordem inversa.(FEITO)
'''
numeros_reais = [12,34,54,65,76,87,98,123,143,245,345,547,655,]
numeros_reais.reverse()
print(numeros_reais)
'''

# Faça um Programa que leia 4 notas, mostre as notas e a média na tela.(FEITO)
'''
"""Nesse exercicio tentei usar o metodo round() para fazer o arredondamento da lista, porém o metodo não funciona em lista"""
notas = [2.23,3.5,5.4,5.7,6.7,8.7,7.8]
print(notas)
media = sum(notas) / len(notas) 
print(f'A média das notas da lista é: {media:.2f}')
'''
# Faça um Programa que leia um vetor de 10 caracteres, e diga quantas consoantes foram lidas. Imprima as consoantes.(FEITO)
'''
"""Precisei utilizar o laço for, pois não é possivel utilizar o metodo 'not in' em uma variavel e retorna em uma string com os valores, pois retorna valores booleanos (True / False)
Peguei os caracteres utilizar o laço para verificar indice por indice e adicionar a lista aquelas que não fossem vogais
"""
caracteres = ['a','c','e','i','o','v','r','t','y','u','p','l','k','j','h','g','f','d','s',]
vogais = ['a', 'e','i','o','u']
print(f'Essas são as consoantes na lista com caracteres: {caracteres not in vogais}')
armazena_consoante = []
for i in caracteres:
    if i not in vogais:
        armazena_consoante.append(i)
    else:
        pass

print(f'Essas são as consoantes na lista com caracteres: {armazena_consoante}')
'''

# Faça um Programa que leia 20 números inteiros e armazene-os num vetor. Armazene os números pares no vetor PAR e os números IMPARES no vetor impar. Imprima os três vetores.(FEITO)

"""Para o laço funcionar corretamente e os valores serem adicionados a lista nesse caso, as listas devem estar fora do loop"""
'''
numeros_inteiros = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
pares = []
impares = []
for numero in numeros_inteiros:
    if numero %2 == 0:
        pares.append(numero)
    else:
        impares.append(numero)

print(f'Esses são os números pares: {pares}')
print(f'Esses são os números impares: {impares}')
''' 

# Faça um Programa que peça as quatro notas de 10 alunos, calcule e armazene num vetor a média de cada aluno, imprima o número de alunos com média maior ou igual a 7.0.(FEITO)
"""
O primeiro loop for recebe o nome do aluno, ainda no primeiro loop, acontece o segundo loop for.

No segundo for: 
- recebe 4 notas do aluno
- as notas do aluno são armazenadas na lista 'armazena_notas'
- a media é calculada na variavel 'media' 

Após o fim do segundo loop for, o primeiro loop continua, nesse loop:
- Ocorre o print do nome do aluno, as 4 notas e a media
- No fim é usado o metodo 'clear()' para limpar a lista e evitar que as notas se acumulem no proximo aluno.
"""
'''
armazena_notas = []
alunos_acima_da_media = []
alunos_abaixo_da_media = []
print(f'Todas as notas: {armazena_notas}')

for nota in range(0+1,5):
    """Primeiro loop for
    metodo clear() -> Usado para limpar a lista e evitar que as notas se acumulem no proximo aluno
    """
    aluno = input(f'\nNome do aluno {nota}: ')

    for n in range(4):
        """Segundo loop for"""
        notas = int(input('Digite as notas dos alunos: '))
        armazena_notas.append(notas)
        media = sum(armazena_notas) / len(armazena_notas)

    print(f'Notas do aluno {aluno}: {armazena_notas}')
    print(f'Média das notas do aluno {aluno}: {media:.2f}')
    armazena_notas.clear()

    if media >= 7:
        """Armazena os alunos acima da media"""
        alunos_acima_da_media.append(aluno)
    
    else:
        """Armazena os alunos abaixo da media"""
        alunos_abaixo_da_media.append(aluno)

print()
print(f'Lista dos alunos com media maior ou igual a 7.0: {alunos_acima_da_media}')
print(f'Lista dos alunos com media maior ou igual a 7.0: {alunos_abaixo_da_media}')
'''

# Faça um Programa que leia um vetor de 5 números inteiros, mostre a soma, a multiplicação e os números.
"""Metodo prod() -> Importado da biblioteca Math, utilizei para realizar a multiplicaçã dos valores da lista"""
'''
numeros_inteiros = [2,2,2,2,2]
print(f'Numeros: {numeros_inteiros}')
print(f'Soma os números: {sum(numeros_inteiros)}')
print(f'Multiplicação: {prod(numeros_inteiros):.2f}')
'''


# Faça um Programa que peça a idade e a altura de 5 pessoas, armazene cada informação no seu respectivo vetor. Imprima a idade e a altura na ordem inversa a ordem lida. (FEITO)
'''
armazena_pessoa = []
armazena_idade = []
armazena_altura = []

for nota in range(0+1,6):
    """Recebo os valores nome, idade e altura e armazeno em suas respectivas listas
    """
    pessoa = input(f'\nNome da Pessoa {nota}: ')
    idade = int(input(f'Idade do(a) {pessoa}: '))
    altura = float(input(f'Altura do(a) {pessoa}: ')) / 100
    # print(f'Nome da pessoa: {pessoa}\nIdade do(a) {pessoa}: {idade}\n Altura:{altura}')
    armazena_pessoa.append(pessoa)
    armazena_idade.append(idade)
    armazena_altura.append(altura)

print(armazena_pessoa)
print(armazena_idade)
print(armazena_altura)
print(f'\nInformações Invertidas abaixo!')
armazena_pessoa.reverse()
armazena_idade.reverse()
armazena_altura.reverse()
print(armazena_pessoa)
print(armazena_idade)
print(armazena_altura)
'''

# Faça um Programa que leia um vetor A com 10 números inteiros, calcule e mostre a soma dos quadrados dos elementos do vetor.(FEITO)
'''
numeros_inteiro = [1,2,3,4,5,6,7,8,9,10]

for n in numeros_inteiro:
    quadrado = n * n
    print(f'Quadrado do número {n}: {quadrado}')
'''

# Faça um Programa que leia dois vetores com 10 elementos cada. Gere um terceiro vetor de 20 elementos, cujos valores deverão ser compostos pelos elementos intercalados dos dois outros vetores. (NÃO TERMINEI ESSE)
'''
numeros1 = [1,3,5,7,9,11,13,15,17,19]
numeros2 = [2,4,6,8,10,12,14,16,18,20]

lista_mesclada = [0]     

for n1 in numeros1:
    lista_mesclada.insert(1,n1)
    for n2 in numeros2:
        lista_mesclada.insert(1,n2)

print(lista_mesclada)
'''