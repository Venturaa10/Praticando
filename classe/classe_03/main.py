from biblioteca import Livro

livro1 = Livro('Sherlock Holmes', 'Sherlock', 2000)
print(livro1.emprestar())
print(livro1.informacoes())
print(livro1.emprestar())
print(livro1.devolver())
print(livro1.informacoes())
print('\nx' * 2)

livro2 = Livro('Bobos e Bocos', 'Alisson', 2010)
print(livro2.devolver())
print(livro2.informacoes())

Livro.exibe_biblioteca()



