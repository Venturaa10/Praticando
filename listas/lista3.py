import os
import random
os.system('cls')

# 1 - Em uma competição de salto em distância cada atleta tem direito a cinco saltos. O resultado do atleta será determinado pela média dos cinco valores restantes. Você deve fazer um programa que receba o nome e as cinco distâncias alcançadas pelo atleta em seus saltos e depois informe o nome, os saltos e a média dos saltos. O programa deve ser encerrado quando não for informado o nome do atleta. A saída do programa deve ser conforme o exemplo abaixo:
# Atleta: Rodrigo Curvêllo
 
# Primeiro Salto: 6.5 m
# Segundo Salto: 6.1 m
# Terceiro Salto: 6.2 m
# Quarto Salto: 5.4 m
# Quinto Salto: 5.3 m

# Resultado final:
# Atleta: Rodrigo Curvêllo
# Saltos: 6.5 - 6.1 - 6.2 - 5.4 - 5.3
# Média dos saltos: 5.9 m

armazena_nome = []
armazena_saltos = []
encerra = 0

print('''
-----------------> COMPETIÇÃO SALTO A DISTÂNCIA <-----------------
''')
print('Caso queira encerrar a listagem dos atletas basta aperta "ENTER" na hora de preencher o nome do atleta!\n')
for n in range(100):
    atleta = input('Nome do atleta: ').capitalize().strip()
    if len(atleta) == 0:
        print('PROGRAMA ENCERRADO!')
        break

    print()
    armazena_nome.append(atleta)

    for s in range(0,5):
        s = s + 1
        salto = random.uniform(0.0,8.0)
        salto = round(salto,2)
        print(f'{s}º Saldo do {atleta}: {salto}')
        # salto = float(input(f'{s}º Saldo do {atleta}: '))

        while salto <= 0 or salto > 7.5:
            print(f'O valor {salto} m é inválido! ')
            print(f'Preencha o {s}º salto novamente!\n')
            salto = float(input(f'{s}º Saldo do {atleta}: '))
        else:
            armazena_saltos.append(salto)

    print()

print(armazena_nome)
print(armazena_saltos)
print()
print(f'Informações dos Atletas!')
for a in armazena_nome:
    print(f'Nome do Atleta: {a}')
    print(f'Saltos do {a} em Metros')
    for indice, s in enumerate(armazena_saltos):
        print(f'{indice+1}º Salto: {s} m')    
    print()
    