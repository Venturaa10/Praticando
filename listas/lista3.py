import os
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

for n in range(0,5):
    atleta = input('Nome do atleta: ').capitalize()
    print()
    armazena_nome.append(atleta)
    for s in range(0,5):
        salto = float(input(f'{s+1}º Saldo do {atleta}: ')) 
        armazena_saltos.append(salto)
    
    break
print(armazena_nome)
print(armazena_saltos)
        
for a in armazena_nome:
    print()
    print(f'Atleta: {a}\n')
    for indice, num in enumerate(armazena_saltos):
        pass
        for sa in armazena_saltos:
            print(f'{indice+1}º salto : {sa} m')
    break