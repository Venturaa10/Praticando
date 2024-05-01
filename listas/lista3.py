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

armazena_saltos = []
encerra = 0

print('''
-----------------> COMPETIÇÃO SALTO A DISTÂNCIA <-----------------
''')
print('Caso queira encerrar a listagem dos atletas basta aperta "ENTER" na hora de preencher o nome do atleta!\n')


for n in range(100):
    """Recebe o nome do atleta"""
    atleta = input('Nome do atleta: ').capitalize().strip()
    """Se o usuario digitar nenhum valor, a lista será encerrada"""
    if len(atleta) == 0:
        print('LISTAGEM ENCERRADO!')
        break
    """
        Laço de repetição responsavel por pedir os 5 saltos do usuario
        Saltos gerados e validados de forma automatica para ajudar a realizar os testes do código com mais rapido
    """
    for s in range(0,5):
        s = s + 1
        """Variaveis utilizadas para realizar testes no código, pois gera os valores de forma automatica tornando a manutenção do código mais rapida"""
        # salto = random.uniform(0.0,8.0)
        # salto = round(salto,2)

        salto = float(input(f'{s}º Saldo do {atleta}: '))
        # print(f'{s}º Saldo do {atleta}: {salto:.2f}')
        
        """
        Enquanto for gerado um valor que retorne esse loop while True, será gerado um novo valor do 'salto' até retornar o loop while, False
        Se não, o valor gerado será armazenado a lista dos saltos
        """
        while salto <= 0 or salto > 7.5:
            print(f'O valor {salto} m é inválido! ')
            print(f'Preencha o {s}º salto novamente!\n')
            
            """Variaveis utilizadas para realizar testes no código, pois gera os valores de forma automatica tornando a manutenção do código mais rapida"""
            # salto = random.uniform(0.0,8.0)
            # salto = round(salto,2)

            salto = float(input(f'{s}º Saldo do {atleta}: '))
            # print(f'{s}º Saldo do {atleta}: {salto:.2f}')
            
        else:
            armazena_saltos.append(salto)


    media = sum(armazena_saltos) / len(armazena_saltos)

    """Laços responsaveis por imprimir as informações do atleta, nome, saltos e media dos saltos."""

    print(f'\nInformações do(a) Atleta {atleta}!\n')
    for indice, salto in enumerate(armazena_saltos):
        print(f'{indice+1}º Salto: {salto} m')
    
    print()

    """Exibindo as informações
    O 'end=' é para não pular linha e os valores dos saltos serem impressos na mesma linha, sendo assim exibido conforme o exercicio
    """
    print(f'Atleta: {atleta}')
    print('Saltos: ',end='')
    """Imprimindo os valores dos saltos"""
    for v in armazena_saltos:
        print(v, end=' - ')

    print(f'\nMédia dos Saltos: {round(media,2)}') 
    
    """Limpando a lista para receber as informações de um novo atleta"""
    armazena_saltos.clear()

    print()
    print('PROXIMO ATLETA!')
