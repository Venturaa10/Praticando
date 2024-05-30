'''
Exercício 1: Criação de uma Classe Básica
Crie uma classe chamada Pessoa que tenha os atributos nome e idade. Implemente um método mostrar_info() que imprime o nome e a idade da pessoa. (Feito)

Exercício 2: Adição de um Método para Atualizar a Idade
Modifique a classe Pessoa do Exercício 1 para incluir um método atualizar_idade() que permite atualizar a idade da pessoa.

Exercício 3: Herança de Classes
Crie uma classe chamada Aluno que herde da classe Pessoa do Exercício 1. Adicione um atributo adicional chamado matricula e um método mostrar_matricula() que imprime a matrícula do aluno.

Exercício 4: Sobrescrita de Métodos
Na classe Aluno do Exercício 3, sobrescreva o método mostrar_info() para incluir a matrícula do aluno.

Estes exercícios fornecem uma base sólida para começar a trabalhar com classes em Python, abrangendo desde a criação básica de classes até conceitos mais avançados como herança e sobrescrita de métodos.
'''

class Pessoa:
    ''' init é um metodo construtor'''
    def __init__(self,nome,idade):
        '''Atributos'''
        self.nome = nome
        self.idade = idade
    
    def mostrar_info(self):
        print(f'Nome: {self.nome} | Idade: {self.idade}')

    def __str__(self):
        return f'Nome: {self.nome} | Idade: {self.idade}'
        
p1 = Pessoa('João',20)
print(p1) # Imprimindo com o metodo especial str
p1.mostrar_info() #Imprimindo utilizando o metodo mostrar_info


