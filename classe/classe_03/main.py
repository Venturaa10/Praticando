from biblioteca import Livro

livro1 = Livro('Sherlock Holmes', 'Sherlock', 2000)
print(livro1.emprestar())
# print(livro1.informacoes())
print(livro1.emprestar())
print(livro1.devolver())
# print(livro1.informacoes())
print()

livro2 = Livro('Bobos e Bocos', 'Alisson', 2010)
print(livro2.devolver())
print(livro2.emprestar())
# print(livro2.informacoes())

# print('TESTE DATA')
# print(livro1.data_emprestimo_formatada)
# print(livro2.data_emprestimo_formatada)

print('TESTE')
Livro.exibe_biblioteca() # Exibe todos os livros da biblioteca


