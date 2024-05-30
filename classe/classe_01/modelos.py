
import os
os.system('cls')

'''
Exercício 1: Criação de uma Classe Básica
Crie uma classe chamada Pessoa que tenha os atributos nome e idade. Implemente um método mostrar_info() que imprime o nome e a idade da pessoa. (Feito)

Exercício 2: Adição de um Método para Atualizar a Idade
Modifique a classe Pessoa do Exercício 1 para incluir um método atualizar_idade() que permite atualizar a idade da pessoa. (Feito)

Exercício 3: Herança de Classes
Crie uma classe chamada Aluno que herde da classe Pessoa do Exercício 1. Adicione um atributo adicional chamado matricula e um método mostrar_matricula() que imprime a matrícula do aluno.

Exercício 4: Sobrescrita de Métodos
Na classe Aluno do Exercício 3, sobrescreva o método mostrar_info() para incluir a matrícula do aluno.

Estes exercícios fornecem uma base sólida para começar a trabalhar com classes em Python, abrangendo desde a criação básica de classes até conceitos mais avançados como herança e sobrescrita de métodos.
'''

class Pessoa:
    def __init__(self,nome,idade):
        ''' init é um metodo construtor que contém os atributos da classe'''
        self.nome = nome
        self.idade = idade
    
    def mostrar_info(self):
        '''Imprime as informações da Pessoa'''
        print(f'Nome: {self.nome} | Idade: {self.idade}')
    
    def atualizar_idade(self):
        '''Atualiza a idade da Pessoa'''
        nova_idade = int(input('Nova idade: '))
        while True:
            if nova_idade > 0 and nova_idade < 100:
                print(f'Idade do(a) {self.nome} atualizada!')
                self.idade = nova_idade 
                break
            else:
                print(f'A idade {nova_idade} não é valida')
                break

    def __str__(self):
        ''''''
        return f'Nome: {self.nome} | Idade: {self.idade}'

class Aluno(Pessoa):
    '''Classe Aluno que herda da classe Pessoa'''
    def __init__(self,nome, idade ,matricula):

        super().__init__(nome,idade)
        self.matricula = matricula 

    def mostrar_matricula(self):
        print(f'Matricula: {self.matricula}')

    def __str__(self):
        return f'Nome: {self.nome} | Idade: {self.idade} | Nº Matricula: {self.matricula}'
        
p1 = Pessoa('João',20)
print(p1) # Imprimindo com o metodo especial str
p1.mostrar_info() #Imprimindo utilizando o metodo mostrar_info

p1.atualizar_idade() 
print(p1) #Exibindo a Pessoa com a idade atualizada

a1 = Aluno('Vinicius',18,2133)
a1.mostrar_matricula()
print(a1)


