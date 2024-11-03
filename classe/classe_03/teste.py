import random
from biblioteca import Biblioteca
from livro import Livro
from cliente import Cliente

# teste_cliente = Cliente('João victor', '18159292783')
# print(Biblioteca.adiciona_cliente_ao_sistema(teste_cliente))
teste_cliente2 = Cliente('Vincius', '123.456.789-09','joao.victor@gmail.com.br')
print(teste_cliente2)
print(Biblioteca.adiciona_cliente_ao_sistema(teste_cliente2))
print(Biblioteca.exibe_clientes())

livro1 = Livro('Sherlock holmes', 'Sherlock', 2000)
# print(Biblioteca.adiciona_livro_na_biblioteca(livro1)) 
# print(livro1.emprestar()) # Funcionando conforme esperado
# print(livro1.emprestar()) # Funcionando conforme esperado
# print(livro1.verifica_data_devolucao()) # Não esta funcionando
# print(livro1.info_livro()) # Funcionando conforme esperado
# print(livro1.devolver()) # Funcionando conforme esperado
# print(livro1.info_livro()) # Funcionando conforme esperado

# livro2 = Livro('Bobos e bocos', 'Alisson rodrigues', 2010)

# print('TESTE') # Aqui esta OK
# print(Biblioteca.exibe_biblioteca()) # Exibe todos os livros da biblioteca


