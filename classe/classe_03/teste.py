import random
from biblioteca import Biblioteca
from livro import Livro
from cliente import Cliente

    
# teste_cliente = Cliente('João victor', '18159292783')
# print(Biblioteca.adiciona_cliente_ao_sistema(teste_cliente))
# teste_cliente2 = Cliente('Vincius', '123.456.789-09')
# print(Biblioteca.adiciona_cliente_ao_sistema(teste_cliente2))
# print(Biblioteca.exibe_clientes())

livro1 = Livro('Sherlock holmes', 'Sherlock', 2000)
# print(livro1.emprestar()) # Funcionando conforme esperado
# print(livro1.info_livro()) # Funcionando conforme esperado
print()

livro2 = Livro('Bobos e bocos', 'Alisson rodrigues', 2010)
print(Biblioteca.adiciona_livro_na_biblioteca(livro2))
# print(livro2.verifica_data_emprestimo())
# print(livro2.verifica_data_devolucao())
# print(livro2.emprestar()) # Funcionando conforme esperado
# print(livro2.emprestar()) # Funcionando conforme esperado
# print(livro2.info_livro())
# print(livro2.devolver()) # Funcionando conforme esperado

# print(Biblioteca.adiciona_livro_na_biblioteca(livro1)) 


print('TESTE DATA') # Verificar
# print(livro1.verifica_data_emprestimo())
# print(livro2.verifica_data_emprestimo())

print('TESTE') # Aqui esta OK
print(Biblioteca.exibe_biblioteca()) # Exibe todos os livros da biblioteca


