import os
os.system('cls')
print('ESSA LISTA DE EXERCICIOS FOI FINALIZADA COM SUCESSO NO DIA 11/04 \n PARABÉNS PELA DEDICAÇÃO \n BORA PRA PROXIMA :)')

# Faça um programa que peça uma nota, entre zero e dez. Mostre uma mensagem caso o valor seja inválido e continue pedindo até que o usuário informe um valor válido. (FEITO)
'''
nota = int(input('Digite uma nota de 0 a 10: '))

if nota < 0 or nota > 10:
    print('Nota Invalida!')
else:
    print('Nota Valida!')
'''
# Faça um programa que leia um nome de usuário e a sua senha e não aceite a senha igual ao nome do usuário, mostrando uma mensagem de erro e voltando a pedir as informações. (FEITO)
'''
nome = input('Nome de Usuario: ')
senha = input('Senha: ')
""" lower -> Retorna a string minuscula"""
if nome.lower() == senha.lower():
    print('A senha não pode ser igual ao nome de usuario!')

else:
    print('Senha Valida!')
'''

# Faça um programa que leia e valide as seguintes informações: (FEITO)
# Nome: maior que 3 caracteres;
# Idade: entre 0 e 150;
# Salário: maior que zero;
# Sexo: 'f' ou 'm';
# Estado Civil: 's', 'c', 'v', 'd'
'''
def limpa_terminal():
    os.system('cls')

def nome_usuario(): 
    global nome
    nome = input('Digite o seu nome: ')
    if len(nome) <= 3:
        limpa_terminal()
        print('Nome Invalido! \n O nome deve conter mais de 3 caracteres.\n')
        return nome_usuario()
    else:
        limpa_terminal()
        validado_msg()


def idade_usuario():
    global idade
    idade = int(input('Digite a sua idade: '))
    if idade < 0 or idade > 150:
        limpa_terminal()
        print('Idade Invalida! \n Maior que o normal')
        return idade_usuario()
    else:
        limpa_terminal()
        validado_msg()

def salario_usuario():
    global salario
    salario = float(input('Salario: R$ '))
    if salario <= 0:
        limpa_terminal()
        print('Salario Invalido! \n Abaixo do normal.')
        return salario_usuario()
    else:
        limpa_terminal()
        validado_msg()

def sexo_usuario():
    global sexo
    sexo = input('Digite M para Masculino ou F para Feminino: ').upper()

    if sexo == 'M' or sexo == 'F':
        limpa_terminal()
        validado_msg()
    else:
        limpa_terminal()
        print(f'{sexo} Invalido!')
        return sexo_usuario()

def estado_civil_usuario():
    global estado_civil
    estado_civil = input("""
        S -> Solteiro
        C -> Casado
        V -> Viuvo
        D -> Divorciado
Estado Civil: """).upper()
    if estado_civil == 'S' or estado_civil == 'C' or estado_civil == 'V' or estado_civil == 'D':
        limpa_terminal()
        validado_msg()

    else:
        limpa_terminal()
        print(f'{estado_civil} Invalido!')
        return estado_civil_usuario()

def validado_msg():
    print('Validado!')

def ficha_do_usuario():
    
    print(f"""
    USUARIO CADASTRADO COM SUCESSO!
          
        Nome: {nome}
        Idade: {idade}
        Salario: R$ {salario}
        Sexo: {sexo}
        Estado Civil: {estado_civil}
""")
    
def recebendo_valores():
    nome_usuario()
    idade_usuario()
    salario_usuario()
    sexo_usuario()
    estado_civil_usuario()

def validando_info():
    recebendo_valores()
    ficha_do_usuario()

validando_info()        
        
'''


# Supondo que a população de um país A seja da ordem de 80000 habitantes com uma taxa anual de crescimento de 3% e que a população de B seja 200000 habitantes com uma taxa de crescimento de 1.5%. Faça um programa que calcule e escreva o número de anos necessários para que a população do país A ultrapasse ou iguale a população do país B, mantidas as taxas de crescimento. (FEITO)
"""
Pais A: 80.000 Habitantes - Taxa anual: 3%
Pais B: 200.000 Habitantes - Taxa anual: 1.5%
"""
'''
a = 80.000
b = 200.000
ano = 0
indice = a < b

while a < b:
    """Enquanto a for menor que b, o laço continuará sendo executado"""
    a = a + (a * 0.03)
    b = b + (b * 0.015)
    ano += 1
print(ano)
print(f'{a:.2f}')
print(f'{b:.2f}')
print(f'Levará cerca de {ano} anos para que a população A ultrapasse B em habitantes.\n Hoje População A: 80.000 Habitantes | População B: 200.000 Habitantes\n Após {ano} anos: População A: {a:.3f} Habitantes | População B:{b:.3f} Habitantes')
'''

# Altere o programa anterior permitindo ao usuário informar as populações e as taxas de crescimento iniciais. Valide a entrada e permita repetir a operação.
'''
a = int(input('Informe a população A: '))
b = int(input('Informe a população B: '))
ano = 0
indice = a < b
taxa_de_a = float(input('Digite a taxa de Crescimento da população A: ')) / 100
taxa_de_b = float(input('Digite a taxa de Crescimento da população B: ')) / 100
while a < b:
    """Enquanto a for menor que b, o laço continuará sendo executado"""
    a = a + (a * taxa_de_a)
    b = b + (b * taxa_de_b)
    ano += 1
print(ano)
print(f'{a:.2f}')
print(f'{b:.2f}')
print(f'Levará cerca de {ano} anos para que a população A ultrapasse B em habitantes.\n Hoje População A: 80.000 Habitantes | População B: 200.000 Habitantes\n Após {ano} anos: População A: {a:.3f} Habitantes | População B:{b:.3f} Habitantes')
'''
# Faça um programa que imprima na tela os números de 1 a 20, um abaixo do outro. Depois modifique o programa para que ele mostre os números um ao lado do outro.(FEITO)

'''
for i in range(0, 21):
    print(i)
"""
Peguei a solução de tirar a quebra de linha no github
Transformando o range em lista os valores retornaram um ao lado do outro
"""
print(list(range(0,21)))
'''

# Faça um programa que leia 5 números e informe o maior número.(FEITO)
'''
num = [25,465,4214,14,2124,214]
lista = []
for i in num:
    """ "armazena" é igual o valor de "i", logo a "lista" vai receber todos os valores da variavél "armazena", conforme o loop é executado o "armazena" recebe outro valor, porém os valores anteriores já foram adicionados a variavel "lista". Então no fim do loop a "lista" armazena terá todos os valores que passaram pela variavle "armazena", armazenados em sua lista."""
    armazena = i
    lista.append(armazena)
    print(f'Número {i} adicionado a lista \n Lista atualizada: {lista}')
    
print(f'\nO maior valor da Lista: {max(lista)}')
'''

# FALTA ESSE 
# Faça um programa que leia 5 números e informe a soma e a média dos números. (FEITO)
'''
numeros = [25,75,85,32,53,64]
lista_armazena = []
for i in numeros:
    """ Conforme o 'i' vai percorrendo a lista 'numeros', a variavel 'armazena' vai recebendo o valor de 'i' e adicionando a lista 'lista_armazena'. 
    No do loop usei os metodos para saber a soma da lista, a media e printei a lista completa.
    """
    armazena = i
    lista_armazena.append(armazena)

print(f'Lista Completa: {lista_armazena}')
print(f'Soma da lista: {sum(lista_armazena)}')
print(f'Média da lista: {sum(lista_armazena) / len(lista_armazena):.2f}')
'''

# FALTA ESSE 
# Faça um programa que imprima na tela apenas os números ímpares entre 1 e 50. (FEITO)
'''
for i in range(0, 51):
    if i %2 :
        print(f'Impar: {i}')
    else:
        pass
'''


# Faça um programa que receba dois números inteiros e gere os números inteiros que estão no intervalo compreendido por eles.(FEITO)

'''
a = int(input('Número 01: '))
b = int(input('Número 02: '))

for i in range(a, b):
    """Enquanto i + 1 for maior que a e menor que b, o número continuara sendo imprimido, assim imprimindo todos os números entre  a e b
    Atenção: Para o código funcionar o valor do a deve ser maior que o valor do b. -> Tratar esse erro
    """
    i += 1
    if i > a and i < b:
        print(i)
    else:
        print(f'TODOS OS NÚMEROS ENTRE {a} E {b} FORAM IMPRIMIDOS')

''' 