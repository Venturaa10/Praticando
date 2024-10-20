import os 
import random
from validate_docbr import CPF
from datetime import datetime, timedelta

os.system('cls')

class Biblioteca:
    livros = {}
    clientes = {}

    @property
    def data_devolucao(self):
        if not self.verifica_livro_cadastro():
            if self._disponivel:
                return self.mensagem_livro_disponibilidade()
            else:
                data_devolucao = self._data_emprestimo + timedelta(days=7)
                return data_devolucao.strftime('%d/%m/%Y') 

    def mensagem_livro_disponibilidade(self):
        ''' Responsavel por exibir uma mensagem sobre a disponibilidade do livro '''
        if self._disponivel:
            return f'O livro "{self.titulo}" está disponivel!'
        else:
            return f'O livro "{self.titulo}" não está disponivel!'
            
    def verifica_livro_cadastro(self):
        ''' Verifica se o atributo _codigo_livro é False, isso indica que o livro não foi cadastrado no sistema '''        
        if self._codigo_livro == False:
            raise ValueError('O livro ainda não foi cadastrado no sistema!')

    def emprestar(self):
        ''' Verifica e realiza a operação de emprestimo de um livro'''
        if not self.verifica_livro_cadastro():
            if self._disponivel:
                self._disponivel = False
                self._data_emprestimo = datetime.today()
                return f'Livro "{self.titulo}" emprestado no dia {self.data_emprestimo}, tenha uma otima leitura :)'
            else:
                return self.mensagem_livro_disponibilidade()

    def devolver(self):
        ''' Realiza a devolução do livro, se o livro estiver realmente emprestado '''
        if not self.verifica_livro_cadastro():
            if self._disponivel:
                return self.mensagem_livro_disponibilidade()
            else:    
                self._disponivel = True
                return f'Livro "{self.titulo}" devolvido a biblioteca!'        

    def verifica_data_devolucao(self):
        ''' Verifica a data de devolução do livro '''
        if not self.verifica_livro_cadastro():
            if self._disponivel:
                return self.mensagem_livro_disponibilidade()
            else:
                return f'Data do Emprestimo: {self.data_emprestimo} | Data de Devolução: {self.data_devolucao}'
            

    def verifica_data_emprestimo(self):
        # Verificar Metodo
        if not self.verifica_livro_cadastro():
            if self._disponivel:
                return self.mensagem_livro_disponibilidade()
            else:
                self._data_emprestimo = datetime.today().strftime('%d/%m/%Y')
                return f'Data emprestimo:{self._data_emprestimo}'
        

    def info_livro(self):
        ''' Exibe as informações do livro'''
        if not self.verifica_livro_cadastro():
            if self._disponivel:
                return f'Código do Livro: {self.codigo_livro} | Titulo: {self.titulo} | Autor: {self.autor} | Ano de Publicação: {self.ano_publicacao} | Disponibilidade: {self.disponivel}'
            else:
                return f'Código do Livro: {self.codigo_livro} | Titulo: {self.titulo} | Autor: {self.autor} | Ano de Publicação: {self.ano_publicacao} | Disponibilidade: {self.disponivel} | Data de Devolução: {self.data_devolucao}'

        
    def info_cliente(self):
        ''' Exibe as informações do cliente'''
        return f'Cliente: {self.nome_cliente} | CPF: {self.cpf_cliente}'


    def gerar_codigo(self):
        ''' Gera o codigo do livro '''
        return random.randint(10000, 100000)

    def adiciona_livro_na_biblioteca(self):
        ''' Tenho que adicionar corretamente as informações do livro no dicionario livro '''
        self._codigo_livro = self.gerar_codigo()
        self._disponivel = True
        Biblioteca.livros[self._codigo_livro] = { # Adicionando o livro no dicionario de "livros"
            'codigo': self.codigo_livro,
            'titulo': self.titulo,
            'autor': self.autor,
            'disponivel': self.disponivel
        }
        return f'Livro: {self.titulo} | Código do Livro: {self.codigo_livro} -> Adicionando à biblioteca'

    def adiciona_cliente_ao_sistema(self):
        ''' Adiciona o cliente ao dicionario "clientes" '''
        Biblioteca.clientes[self.cpf_cliente] = {
            'nome': self.nome_cliente,
            'cpf': self.cpf_cliente
        }
        return f'Nome do Cliente: {self.nome_cliente} | CPF: {self.cpf_cliente} -> Cadastrado no sistema'


    @classmethod # Metodo estatico, permite acessar os atributos da classe sem precisar instanciá-la.
    def exibe_biblioteca(cls):
        ''' Retorna as informações de todos os livros da biblioteca '''
        livros_lista = []
        if not cls.livros:
            return 'A biblioteca está vazia :('

        for livro, info in cls.livros.items():
            '''Pega os pares de chave e valor do dicionário cls.livros (onde a chave é o identificador do livro e o valor é outro dicionário contendo informações sobre o livro), e adiciona uma string formatada com os detalhes do livro na lista "livros_lista".'''
            livros_lista.append(f"Código: {info['codigo']} | Título: {info['titulo']} | Autor: {info['autor']} | Disponibilidade: {info['disponivel']}")

        return '\n'.join(livros_lista) # Une os itens da lista, porém o \n faz com que seja exibido um abaixo do outro.

    @classmethod
    def exibe_clientes(cls):
        clientes_lista = []
        if not cls.clientes:
            return 'Nenhum cliente encontrado no sistema!'

        for cliente, info in cls.clientes.items():
            clientes_lista.append(f"CPF: {info['cpf']} | Nome Completo: {info['nome']}")

        return '\n'.join(clientes_lista) # Une os itens da lista, porém o \n faz com que seja exibido um abaixo do outro.
    
