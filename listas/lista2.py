import os
import random
os.system('cls')

# 1 - Foram anotadas as idades e alturas de 30 alunos. Faça um Programa que determine quantos alunos com mais de 13 anos possuem altura inferior à média de altura desses alunos.

'''
def listas():
    global nomes
    global aluno_lista
    global altura_lista
    global idade_lista
    global acima_da_media
    global abaixo_da_media
    global aluno_maior_13
    global aluno_menores_13

    nomes = ['João','Vinicius','Maria','Paula','Jessica','Patrick','Romeu','Isabelle']
    aluno_lista = []
    altura_lista = []
    idade_lista = []

    acima_da_media = []
    abaixo_da_media = []

    aluno_menores_13 = []
    aluno_maior_13 = []

def primeiro_loop():
    global media_altura
    """ Primeiro Loop for"""
    for a in nomes:
        print()
        info_aluno()
        verifica_altura(altura)
        # verifica_idade()

        media_altura = sum(altura_lista) / len(altura_lista)
        
    return media_altura,a

def segundo_loop():
    """ Segundo Loop for"""
    for a in aluno_maior_13:
        if altura > media_altura:
            acima_da_media.append(aluno)
        else:
            abaixo_da_media.append(aluno)

def gera_nome():
    """Retornando o aluno, pois preciso do valor da variavel"""
    global aluno
    aluno = random.choice(nomes)
    if aluno in aluno_lista == True:
        return gera_nome()
    else: 
        pass

    return aluno

def gerando_altura():
    """Gerando a altura do aluno"""
    gera_altura = random.uniform(1.50,2.00)
    altura = round(gera_altura,2)

    return altura

def info_aluno():
    """Gerando a altura através do rando.uniform, retornando um valor maior que o primeiro parametro e menor que o segundo parametro
    Na variavel 'altura' ocorre o tratamento da variavel 'gera_altura' para retornar um valor com duas casas decimais
    """
    global idade
    global altura

    aluno = gera_nome()
    altura = gerando_altura()
    idade = random.randint(6,18)
    verifica_idade()
    print(f'Aluno(a) {aluno} foi cadastrado!')
    armazena_info()

    print(f'Aluno(a): {aluno}')
    print(f'Altura do(a) {aluno}: {altura:.2f}')
    print(f'Idade do(a) {aluno}: {idade}')
    
def armazena_info():
    """Adicionando as informações nome, altura e idade do aluno em suas respectivas listas"""
    aluno_lista.append(aluno)
    altura_lista.append(altura)
    idade_lista.append(idade)

def verifica_altura(altura):
    """Se a altura do aluno for menor 1.50 ou 2.00 será gerado uma nova altura para o aluno """
    if altura < 1.50 or altura > 2.00:
        gerando_altura()
    else:
        pass

def verifica_idade():
    """Se a idade do aluno for maior que 13, será adicionado na respectiva lista, se não será adicionado em outra lista"""
    if idade >= 13:
        aluno_maior_13.append(aluno)
    else: 
        aluno_menores_13.append(aluno)


def imprime_infos():
    print()
    print(aluno_lista)
    print(altura_lista)
    print(idade_lista)
        
    print()
    print(f'Média de altura dos alunos: {media_altura:.2f}')
    print(f'Alunos com altura acima da média: {acima_da_media}')
    print(f'Alunos com altura abaixo da média: {abaixo_da_media}')

    print()
    print(f'Alunos não verificados por serem menores que 13 anos: {aluno_menores_13}')
    print(f'Alunos maiores que 13 anos: {aluno_maior_13}')

listas()
primeiro_loop()
segundo_loop()
imprime_infos()
'''


# 2 - Faça um programa que receba a temperatura média de cada mês do ano e armazene-as em uma lista. Após isto, calcule a média anual das temperaturas e mostre todas as temperaturas acima da média anual, e em que mês elas ocorreram (mostrar o mês por extenso: 1 – Janeiro, 2 – Fevereiro, . . . ). (FEITO) Só ficou faltando a parte de imprimir, mas a logica está correta
''' 
temperatura = []
meses = ['Janeiro','Fevereiro','Março','Abril','Maio','Junho','Julho','Agosto','Setembro','Outubro','Novembro','Dezembro']
acima_media = []
abaixo_media = []
temp_acima = []
temp_abaixo = []

for m in meses:
    """Para cada mês, será gerado uma temperatura através do metodo randouniform(valor_minima, valor_maxima)
    round -> Tratandoas casas decimais
    """
    gera_temperatura = random.uniform(5.00,45.00)
    temperatura.append(round(gera_temperatura,2))
    for t in temperatura:
        pass
    
    media_temp = sum(temperatura) / len(temperatura)
    if t > media_temp:
        acima_media.append(m) 
        temp_acima.append(t)       
    else:
        abaixo_media.append(m)
        temp_abaixo.append(t)       

    print(f'Mês: {m} | Temperatura Média: {t}')

print()
print(f'Média anual da temperatura: {media_temp:.2f}')
print()

print(f'Lista dos Acima da Média: {acima_media, temp_acima}')
print(f'Lista dos Abaixo da Média: {abaixo_media, temp_abaixo}')
'''


# 3 - Utilizando listas faça um programa que faça 5 perguntas para uma pessoa sobre um crime. As perguntas são:
# "Telefonou para a vítima?"
# "Esteve no local do crime?"
# "Mora perto da vítima?"
# "Devia para a vítima?"
# "Já trabalhou com a vítima?" 
# O programa deve no final emitir uma classificação sobre a participação da pessoa no crime. Se a pessoa responder positivamente a 2 questões ela deve ser classificada como "Suspeita", entre 3 e 4 como "Cúmplice" e 5 como "Assassino". Caso contrário, ele será classificado como "Inocente". (FEITO)

'''
sim = []
nao = []

print('!RESPONDA COM SIM OU NÃO!')
nome = input('Seu nome: ')
perguntas = ['Telefonou para a vítima? ', 'Esteve no local do crime? ','Mora perto da vítima? ','Devia para a vítima? ', 'Já trabalhou com a vítima? ']

for p in perguntas:
    resposta = input(f'{p}')
    if resposta.upper() == 'S' or resposta.upper() == 'SIM':
        sim.append(resposta)
    elif resposta.upper() == 'N' or resposta.upper() == 'NAO' or resposta.upper() == 'NÃO':
        nao.append(resposta)

print(sim)
print(nao)
respostas_positivas = len(sim)

if respostas_positivas == 2:
    print(f'O(a) {nome} é classificado(a) como: Suspeita')

elif respostas_positivas == 3 or respostas_positivas == 4:
    print(f'O(a) {nome} é classificado(a) como: Cúmplice')

elif respostas_positivas == 5:
    print(f'O(a) {nome} é classificado(a) como: Assassino')

else:
    print(f'O(a) {nome} é classificado(a) como: Inocente')
'''

# 4 - Faça um programa que leia um número indeterminado de valores, correspondentes a notas, encerrando a entrada de dados quando for informado um valor igual a -1 (que não deve ser armazenado). Após esta entrada de dados, faça:

# Mostre a quantidade de valores que foram lidos; (FEITO)
# Exiba todos os valores na ordem em que foram informados, um ao lado do outro; (FEITO)
# Exiba todos os valores na ordem inversa à que foram informados, um abaixo do outro; (FEITO)
# Calcule e mostre a soma dos valores; (FEITO)
# Calcule e mostre a média dos valores; (FEITO)
# Calcule e mostre a quantidade de valores acima da média calculada; 
# Calcule e mostre a quantidade de valores abaixo de sete;
# Encerre o programa com uma mensagem;

armazena_notas = []
acima_media = []
abaixo_de_sete = []
na_media = []
trava = -1

for n in range(0,100):
    """Loop responavél por:
    - Gerar nota aleatoria
    - Verificar a nota gerada se é igual a trava
    """
    gerador = random.randint(trava,10) 
    nota = gerador
    if nota != trava:
        if nota != 0:
            armazena_notas.append(nota)
        else:
            pass

    else:
        print(f'A trava foi acionada! \nTrava: {nota}') 
        break

print() #Pula linha
print(f'Notas geradas na ordem que foram adicionados: {armazena_notas}')

""" Linha comentada abaixo está funcionando corretamente,é da ordem inversa, estava atrapalhando a minha visualização no terminal, então deixei comentada para melhorar a visualização"""
# print(f'Notas geradas na ordem inversa que foram adicionadas:')
# armazena_notas.reverse()
# for nota in armazena_notas:
#     print(nota)

"""Tratamento de erro caso a primeira nota gerada tenha sido valor igual a trava"""
try:
    media_notas = sum(armazena_notas) / len(armazena_notas)
    print(f'Média das notas : {round(media_notas,2)}')
    print(f'Quantidade de Notas armazenadas: {len(armazena_notas)}')
    print(f'Soma das notas: {sum(armazena_notas)}')
except:
    print(f'Nenhuma nota foi gerada\nArmazenamento vazio: {armazena_notas} \nTente Novamente!')
    print()


try:
    for nota in armazena_notas:

        if nota > media_notas:
            acima_media.append(nota)
        elif nota < 7: 
            abaixo_de_sete.append(nota)
        else: 
            na_media.append(nota)        

    print(f'Notas Acima da Média: {acima_media}')
    print(f'Notas Abaixo de Sete: {abaixo_de_sete}')
    print(f'Notas na Média: {na_media}')
    print() #Pula linha

    """Condicional pela mudança da mensagem final, caso nenhuma nota tenha sido adicionada a lista"""
    if len(armazena_notas) != 0:
        print('Geração de notas realizada com sucesso!')
    else:  
        print('A maquina pifou :(')

except:
    pass
