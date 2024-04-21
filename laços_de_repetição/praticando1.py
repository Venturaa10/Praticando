import os
os.system('cls')
print('ESSA LISTA DE EXERCICIOS FOI FINALIZADA COM SUCESSO NO DIA 11/04 \n PARABÉNS PARA MIM PELA DEDICAÇÃO \n BORA PRA PROXIMA :)')

# Contagem regressiva:
# Escreva um programa que solicita um número inteiro positivo do usuário e, em seguida, imprime uma contagem regressiva a partir desse número até 0.(FEITO)
'''
numeroint = int(input('Digite um número positivo: '))

for i in range(numeroint, -1, -1):
    """Começa no numeroint, para no -1 e diminuí de 1 em 1 """
    print(i)
'''

# Soma dos números pares:
# Escreva um programa que solicita um número inteiro positivo do usuário e, em seguida, calcula e imprime a soma de todos os números pares de 0 até esse número. (FEITO)
'''
numero = int(input('Digite um número positivo: '))

for i in range(0,numero+2,2):
    """O +2 é para o número chegar até o número desejado, senão o código para um par antes
    Tratar Erro -> Se o número é impar o par após esse número também está sendo impresso.
    """
    print(i)
'''

# Tabuada:
# Escreva um programa que solicita um número inteiro do usuário e imprime a tabuada desse número até 10. (FEITO)
'''
numero = int(input('Digite um número positivo: '))

for tabuada in range(1,numero+1):
    multiplicacao = tabuada * numero
    texto = f'{tabuada} X {numero} = {multiplicacao}'
    print(texto)

    if tabuada == 10:
        break
'''
# Or
'''
numero = int(input("Digite um número inteiro: "))

for i in range(1, 11):
    print(numero, "x", i, "=", numero * i)
'''

# Fatorial:
# Escreva um programa que calcula o fatorial de um número inteiro positivo dado pelo usuário.
# "2! + 3! = (2 · 1) + (3 · 2 · 1) = 2 + 6 = 8"
'''
numero = int(input("Digite um número inteiro: "))

for i in range(numero - 1):
    calcu = i * (numero - 1)
    resultado = calcu * numero
    texto = resultado
    # calculando = i 
    print(texto)
'''

# Sequência de Fibonacci:
# Escreva um programa que imprime os primeiros N termos da sequência de Fibonacci, onde N é dado pelo usuário.

# Verificação de número primo:
# Escreva um programa que verifica se um número dado pelo usuário é primo ou não.

'''
numero = int(input("Digite um número inteiro positivo: "))
primo = True

if numero <= 1:
    primo = False
else:
    for i in range(2, int(numero**0.5) + 1):
        if numero % i == 0:
            primo = False
            break

if primo:
    print(numero, "é um número primo.")
else:
    print(numero, "não é um número primo.")
'''

# Contagem de vogais:
# Escreva um programa que conta o número de vogais em uma string dada pelo usuário.(FEITO)
'''
string_usuario = input('Digite uma palavra: ')
vogais = ['a','e','i','o','u']
contador = []

for vogal in string_usuario.lower():
    """Variavel 'verifica' -> Tem o papel de verificar se existe a letra na lista 'vogais'
    Se retornar True, essa vogal será armazenada na lista 'contador'
    No final do loop, eu uso o metodo 'len' para verificar a quantidade de itens na lista, ou seja, a quantidade de vogais
    """
    verifica = vogal in vogais
    if verifica == True:
        contador.append(vogal)
        # print(contador)
        

print(f'Quantidade de vogais na frase: {len(contador)}')
'''


# Inversão de string:
# Escreva um programa que recebe uma string do usuário e imprime a string invertida.(FEITO COM CHATGPT :( ESTAVA COM MUITA DIFICULDADE )
'''
"""Para solucionar esse exercicio, busquei o ChatGPT. 
Explicando a resolução Conceito

        Slicingsequencia[início:fim:passo]
início: O índice onde a fatia começa (inclusive).
fim: O índice onde a fatia termina (exclusivo).
passo: O tamanho do passo entre os elementos da fatia (opcional, o padrão é 1).

Ao usar um passo negativo (-1), estamos percorrendo a sequência de trás para frente, resultando na sequência invertida.
"""

string = input("Digite uma string: ")

string_invertida = string[::-1]

print(f'Invertida: {string_invertida}')
'''

# Contagem de letras:
# Escreva um programa que conta o número de ocorrências de cada letra em uma string dada pelo usuário.
'''

frase = input('Digite uma frase: ')
armazena_letras = []
contador_de_letras = 0

for letra in frase.upper():
    verifica_letra_lista = letra not in armazena_letras
    letra_repetida = armazena_letras.count(letra)
    
    if verifica_letra_lista == True:
        armazena_letras.append(frase)
        contador_de_letras +1

print(f'Quantidade de letras contabilizadas: {len(armazena_letras)}')
'''

# Soma de dígitos:
# Escreva um programa que solicita um número inteiro do usuário e calcula a soma de seus dígitos.

'''
numero = int(input("Digite um número inteiro positivo: "))
texto = input('Texto: ')
lista_numero = []
lista_numero.append(numero)
separando = texto.split(',')
print(separando)
for p in lista_numero:
    print(p)
'''