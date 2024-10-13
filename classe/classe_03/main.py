import random
from biblioteca import Biblioteca
from livro import Livro



livro1 = Livro('Sherlock holmes', 'Sherlock', 2000)
print(livro1.emprestar())
# print(livro1.informacoes())
print(livro1.emprestar())
print(livro1.devolver())
# print(livro1.informacoes())
print()

livro2 = Livro('Bobos e bocos', 'Alisson rodrigues', 2010)
print(livro2.devolver())
print(livro2.emprestar())
# print(livro2.informacoes())

# print('TESTE DATA')
# print(livro1.data_emprestimo_formatada)
# print(livro2.data_emprestimo_formatada)

print('TESTE')
Biblioteca.exibe_biblioteca() # Exibe todos os livros da biblioteca


