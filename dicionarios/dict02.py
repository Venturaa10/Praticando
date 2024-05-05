import os
import random
os.system('cls')

# 1- Contagem de Palavras:
# Escreva um programa que recebe uma string como entrada e conta a ocorrência de cada palavra na string. Em seguida, armazene essas contagens em um dicionário onde as chaves são as palavras e os valores são as contagens de ocorrências.
'''
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
'''

# 2 - Mesclar Dicionários Únicos:
# Escreva uma função que aceita uma lista de dicionários como entrada e retorna um único dicionário que contém todas as chaves e seus respectivos valores únicos de todos os dicionários de entrada.
'''
# Acrescentar uma verificação em caso de chaves iguais, qual chave será armazenada, o criterio deve ser decidido baseado no valor das chaves! 
"""As três listas que vou armazenar em uma única lista sem valores repetidos"""
dic1 = {'Primeiro': 1, 'Segundo': 2, 'Terceiro': 3, 'Quarto': 4, 'Quinto':5}
dic2 = {'Sexto': 6, 'Setimo': 7, 'Oitavo': 8, 'Quarto': 4, 'Decimo':10}
dic3 = {'Onze': 11, 'Doze': 12, 'Setimo': 7, 'Quatorze': 14, 'Quinze':15}

"""Lista vai receber as outras listas"""
dic_principal = {}

def recebe_dic(dicionario):
    """Função responsavél pela verificação e armazenamento das informações na lista principal
    Recebe como parametro o dicionario que será armazenado no dicionario principal
    """
    
    """
    Para cada elemento no dicionario, será realizada a seguinte verificação:
    Se o elemento não estiver na lista principal, a chave e o valor da chave serão armazenados dentro da principal 
    Se não, será exibida uma mensagem e o programa continuara
    """
    for v in dicionario:
        
        if v not in dic_principal:
            print(f'Chave "{v}" adicionado(a) ao dicionario principal!')
            valor_chave = dicionario[v]
            dic_principal[v] = valor_chave
        else:
            print(f'Chave "{v}" já existente!')
    
    
    print()
    input(f'VERIFICAÇÃO CONCLUÍDA COM SUCESSO!\n ENTER PARA CONTINUAR')
    print()

recebe_dic(dic1)
recebe_dic(dic2)
recebe_dic(dic3)

print(dic_principal)
'''

# 3 - Média de Notas:
# Escreva um programa que pede ao usuário para inserir o número de alunos em uma turma, seus nomes e suas notas (em uma escala de 0 a 10) como entrada. Em seguida, calcule e imprima a média das notas. Armazene os nomes dos alunos como chaves e suas notas como valores em um dicionário.

""" Melhorias a serem feitas no código

Verificar se as notas inseridas estão dentro do intervalo válido (0 a 10).
Melhorar a interação com o usuário, fornecendo mensagens mais descritivas e instruções claras.
Adicionar tratamento de erros para lidar com entradas inválidas do usuário.
Permitir que o usuário insira os nomes dos alunos em vez de selecioná-los aleatoriamente de uma lista predefinida.
Oferecer opções adicionais, como calcular a nota mais alta ou mais baixa da turma, além da média.
"""

"""Essa lista é apenas para agilizar os testes e não precisar ficar digitando nomes diversas vezes"""
armazena_nome = ['João','Beatriz','Lucas','Jessica','Gabriel','Vinicius','Maria','Pedro','Adriana','Wesley','Eduarda','Patricia']
qtd_alunos = int(input('Quantidade de Alunos na Turma: '))
print()

turma = {}
notas_alunos = []
for aluno in range(0,qtd_alunos):

    aluno = random.choice(armazena_nome)
    if aluno not in turma:
        turma[aluno] = 0
    
    else:
        print(f'{aluno} já está na turma!')
        continue; aluno
    
    for n in range(0,5):
        """Gerando notas automaticamente de maneira aleatorio apenas para agilizar o teste do codigo"""
        nota = random.randint(0,10)
        notas_alunos.append(nota)
        
        print(f'{n + 1}º Nota do(a) {aluno}: {nota}')

    media = sum(notas_alunos) / len(notas_alunos)
    print(f'Média do(a) aluno {aluno}: {media:.2f}')
    print()

    """Limpando a lista que armazena as notas do aluno anterior"""
    notas_alunos.clear()

print(turma)
print(notas_alunos)
    
