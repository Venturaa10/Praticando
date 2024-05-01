import os
import random
os.system('cls')

# 1 - Em uma competição de salto em distância cada atleta tem direito a cinco saltos. O resultado do atleta será determinado pela média dos cinco valores restantes. Você deve fazer um programa que receba o nome e as cinco distâncias alcançadas pelo atleta em seus saltos e depois informe o nome, os saltos e a média dos saltos. O programa deve ser encerrado quando não for informado o nome do atleta. A saída do programa deve ser conforme o exemplo abaixo: (FEITO)
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

'''
armazena_saltos = []
encerra = 0

print("""
-----------------> COMPETIÇÃO SALTO A DISTÂNCIA <-----------------
""")
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
'''

# 2 - Uma grande emissora de televisão quer fazer uma enquete entre os seus telespectadores para saber qual o melhor jogador após cada jogo. Para isto, faz-se necessário o desenvolvimento de um programa, que será utilizado pelas telefonistas, para a computação dos votos. Sua equipe foi contratada para desenvolver este programa, utilizando a linguagem de programação C++. Para computar cada voto, a telefonista digitará um número, entre 1 e 23, correspondente ao número da camisa do jogador. Um número de jogador igual zero, indica que a votação foi encerrada. Se um número inválido for digitado, o programa deve ignorá-lo, mostrando uma breve mensagem de aviso, e voltando a pedir outro número. Após o final da votação, o programa deverá exibir:
# O total de votos computados;
# Os númeos e respectivos votos de todos os jogadores que receberam votos;
# O percentual de votos de cada um destes jogadores;
# O número do jogador escolhido como o melhor jogador da partida, juntamente com o número de votos e o percentual de votos dados a ele.
# Observe que os votos inválidos e o zero final não devem ser computados como votos. O resultado aparece ordenado pelo número do jogador. O programa deve fazer uso de arrays. O programa deverá executar o cálculo do percentual de cada jogador através de uma função. Esta função receberá dois parâmetros: o número de votos de um jogador e o total de votos. A função calculará o percentual e retornará o valor calculado. Abaixo segue uma tela de exemplo. O disposição das informações deve ser o mais próxima possível ao exemplo. Os dados são fictícios e podem mudar a cada execução do programa. Ao final, o programa deve ainda gravar os dados referentes ao resultado da votação em um arquivo texto no disco, obedecendo a mesma disposição apresentada na tela.
# Enquete: Quem foi o melhor jogador?

# Número do jogador (0=fim): 9
# Número do jogador (0=fim): 10
# Número do jogador (0=fim): 9
# Número do jogador (0=fim): 10
# Número do jogador (0=fim): 11
# Número do jogador (0=fim): 10
# Número do jogador (0=fim): 50
# Informe um valor entre 1 e 23 ou 0 para sair!
# Número do jogador (0=fim): 9
# Número do jogador (0=fim): 9
# Número do jogador (0=fim): 0

# Resultado da votação:

# Foram computados 8 votos.

# Jogador Votos           %
# 9               4               50,0%
# 10              3               37,5%
# 11              1               12,5%
# O melhor jogador foi o número 9, com 4 votos, correspondendo a 50% do total de votos.

"""Está lista armazena todos os votos de acordo com o número da camisa do jogador"""

'''
armazena_votos = []

while True:
    """
    - Tratamento de erro caso o usuario digite um valor diferente de um número inteiro, retornando a variavel para digitar outro número
    - O programa só continuara quando receber um valor valido
    """
    try:
        # numero_jogador = int(input('Número do Jogador: '))
        for i in range(0,50):
            numero_jogador = random.randint(0,25)      
    except:
        os.system('cls')
        print('Valor Invalido!')
        continue; numero_jogador

    """Em caso de 0, o programa será encerrado, se for menor que 0 ou maior que 23, retornará uma mensagem de aviso e a para digitar novamente até o usuario digitar um valor valido, se não o voto será computado e armazenado na lista"""
    if numero_jogador == 0:
        print()
        print('PROGRAMA ENCERRADO!')
        break
    elif numero_jogador < 0 or numero_jogador > 23:
        os.system('cls')
        print('Informe um número entre 1 e 23, ou 0 para encerrar!')
        continue; numero_jogador
    else:
        os.system('cls')
        print(f'Voto no número {numero_jogador} computado!')
        armazena_votos.append(numero_jogador)

verifica_repeticao = []
armazena_votos.sort()
numero_vencedor = []
votos_vencedor = []

for voto in armazena_votos:
        """
        - Essa condição é para evitar que seja contabilizado e exibido a votação de um número já contabilizado pelo programa, ou seja, se esse valor (Número do jogador e a quantidade de votos recebidos) não estiver na lista de verificação, ele será contabilizado e armazenado na lista.

        - Caso retorne False, o programa continuara sem duplicar os votos do jogador
        """
        if voto not in verifica_repeticao:
            """ 
            - O Loop adiciona o voto desse jogaodr na lista de verificação
            - Conta a quantidade de votos que o jogador recebeu, utilizando o metodo count, que retornara o número de ocorrencias que o número do jogador tem na lista de 'armazena_votos'
            - Calcula a porcentagem dos votos recebidos 
            """


            for i in range(1):
                verifica_repeticao.append(voto) 
                contador_de_ocorrencia = armazena_votos.count(voto)
                calcula_porcem = contador_de_ocorrencia / len(armazena_votos) * 100
            
            # numero_vencedor.append(voto)
            # votos_vencedor.append(contador_de_ocorrencia)
            # if contador_de_ocorrencia < votos_vencedor.pop():
            #     pass
            # else:
            #     numero_vencedor.clear()
            #     votos_vencedor.clear()

            #     numero_vencedor.append(voto)
            #     votos_vencedor.append(contador_de_ocorrencia)
                

                if voto < 10:
                    print(f'Jogador Número {voto}  | Votos Recebidos: {contador_de_ocorrencia}  | Porcentagem: {calcula_porcem:.2f}%')
                else:
                    print(f'Jogador Número {voto} | Votos Recebidos: {contador_de_ocorrencia}  | Porcentagem: {calcula_porcem:.2f}%')


        else:
            pass


print()   
# print(armazena_votos)
print(f'Foram computados {len(armazena_votos)} votos!')
print(f'Vencedor é o jogador número {numero_vencedor} com {votos_vencedor} votos!')
'''

# 3 - Uma empresa de pesquisas precisa tabular os resultados da seguinte enquete feita a um grande quantidade de organizações:
# "Qual o melhor Sistema Operacional para uso em servidores?"

# As possíveis respostas são:

# 1- Windows Server
# 2- Unix
# 3- Linux
# 4- Netware
# 5- Mac OS
# 6- Outro
# Você foi contratado para desenvolver um programa que leia o resultado da enquete e informe ao final o resultado da mesma. O programa deverá ler os valores até ser informado o valor 0, que encerra a entrada dos dados. Não deverão ser aceitos valores além dos válidos para o programa (0 a 6). Os valores referentes a cada uma das opções devem ser armazenados num vetor. Após os dados terem sido completamente informados, o programa deverá calcular a percentual de cada um dos concorrentes e informar o vencedor da enquete. O formato da saída foi dado pela empresa, e é o seguinte:
# Sistema Operacional     Votos   %
# -------------------     -----   ---
# Windows Server           1500   17%
# Unix                     3500   40%
# Linux                    3000   34%
# Netware                   500    5%
# Mac OS                    150    2%
# Outro                     150    2%
# -------------------     -----
# Total                    8800

# O Sistema Operacional mais votado foi o Unix, com 3500 votos, correspondendo a 40% dos votos.
armazena_escolha = []
def sistema_operacional(nome): 
    print(f'{nome} | Votos Recebidos: {contador_de_ocorrencia}  | Porcentagem: {calcula_porcem:.2f}%')

exibir = ('''
    !Sistemas Operacionais!
    
        1- Windows Server
        2- Unix
        3- Linux
        4- Netware
        5- Mac OS
        6- Outro
      
    0 - Para encerrar o programa
''')


while True:
    """
    - Tratamento de erro caso o usuario digite um valor diferente de um número inteiro, retornando a variavel para digitar outro número
    - O programa só continuara quando receber um valor valido
    """
    try:
        # numero_jogador = int(input('Número do Jogador: '))
        for i in range(0,50):
            # numero_sistema = int(input('Qual o melhor Sistema Operacional para uso em servidores? '))
            numero_sistema = random.randint(0,7)      
    except:
        os.system('cls')
        print(exibir)
        print('Valor Invalido!')
        continue; numero_sistema

    """Em caso de 0, o programa será encerrado, se for menor que 0 ou maior que 23, retornará uma mensagem de aviso e a para digitar novamente até o usuario digitar um valor valido, se não o voto será computado e armazenado na lista"""
    if numero_sistema == 0:
        print()
        print('PROGRAMA ENCERRADO!')
        break
    elif numero_sistema < 0 or numero_sistema > 6:
        os.system('cls')
        print(exibir)
        print('Informe um número entre 1 e 6 de acordo com o sistema operacional de sua preferencia, ou 0 para encerrar!')
        continue;numero_sistema
    else:
        os.system('cls')
        print(exibir)
        print(f'Voto no número {numero_sistema} computado!')
        armazena_escolha.append(numero_sistema)
        continue;numero_sistema

print(armazena_escolha)

verifica_repeticao = []
armazena_escolha.sort()


for voto in armazena_escolha:
        """
        - Essa condição é para evitar que seja contabilizado e exibido a votação de um número já contabilizado pelo programa, ou seja, se esse valor (Número do jogador e a quantidade de votos recebidos) não estiver na lista de verificação, ele será contabilizado e armazenado na lista.

        - Caso retorne False, o programa continuara sem duplicar os votos do jogador
        """
        if voto not in verifica_repeticao:
            """ 
            - O Loop adiciona o voto desse jogaodr na lista de verificação
            - Conta a quantidade de votos que o jogador recebeu, utilizando o metodo count, que retornara o número de ocorrencias que o número do jogador tem na lista de 'armazena_votos'
            - Calcula a porcentagem dos votos recebidos 
            """
            for i in range(1):
                verifica_repeticao.append(voto) 
                contador_de_ocorrencia = armazena_escolha.count(voto)
                calcula_porcem = contador_de_ocorrencia / len(armazena_escolha) * 100

            if contador_de_ocorrencia == 1:
                sistema_operacional('Windows Server')
            elif contador_de_ocorrencia == 2:
                sistema_operacional('Unix')
            elif contador_de_ocorrencia == 3:
                sistema_operacional('Lunix')
            elif contador_de_ocorrencia == 4:
                sistema_operacional('Netware')
            elif contador_de_ocorrencia == 5:
                sistema_operacional('Mac OS')
            elif contador_de_ocorrencia == 6:
                sistema_operacional('Outro')


        else:
            pass

print()
print(f'Foram computados {len(armazena_escolha)} votos!')