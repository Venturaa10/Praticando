import random
from biblioteca import Biblioteca
from livro import Livro
from cliente import Cliente

    
teste_cliente = Cliente('João victor', '18159292783')
print(Biblioteca.adiciona_cliente_ao_sistema(teste_cliente))
teste_cliente2 = Cliente('Vincius', '123.456.789-09')
print(Biblioteca.adiciona_cliente_ao_sistema(teste_cliente2))
print(Biblioteca.exibe_clientes())

livro1 = Livro('Sherlock holmes', 'Sherlock', 2000)

# # print(livro1.emprestar())
# # print(livro1.info_livro())
# # print(livro1.emprestar())
# # print(livro1.info_livro())
# # print()

livro2 = Livro('Bobos e bocos', 'Alisson rodrigues', 2010)
# print(livro2.devolver())
# # print(livro2.emprestar())
# # print(livro2.info_livro())

print(Biblioteca.adiciona_livro_na_biblioteca(livro1))
print(Biblioteca.adiciona_livro_na_biblioteca(livro2))

# print('TESTE DATA')
# print(livro1.data_emprestimo_formatado)
# print(livro2.data_emprestimo_formatado)

print('TESTE')
print(Biblioteca.exibe_biblioteca()) # Exibe todos os livros da biblioteca


