import os 
import random
from validate_docbr import CPF
from datetime import datetime, timedelta

os.system('cls')

class Biblioteca:
    livros = {}
    clientes = {}

    @property
    def data_emprestimo_formatado(self):
        ''' Formata a data para o padrão do Brasil '''
        if self.disponivel:
            self.data_emprestimo = datetime.today()
            return 'O livro está disponivel!'
        else:
            return self.data_emprestimo.strftime('%d/%m/%Y')
    
    def emprestar(self):
        ''' Verifica e realiza a operação de emprestimo de um livro'''
        if self.disponivel:
            self.disponivel = False
            self.data_emprestimo = datetime.today()
            return f'Livro "{self.titulo_formatado}" emprestado no dia {self.data_emprestimo_formatado}, tenha uma otima leitura :)'
        else:
            return f'O livro "{self.titulo_formatado}" não está disponivel!'

    def devolver(self):
        ''' Realiza a devolução do livro, se o livro estiver realmente emprestado '''
        if self.disponivel:
            return f'Não é possivel fazer a devolução, o livro não foi emprestado!'
        else:    
            self.disponivel = True
            return f'Livro "{self.titulo_formatado}" devolvido a biblioteca!'        

    def verifica_data(self):
        ''' Verifica a data de devolução do livro '''
        if self.disponivel:
            return f'O livro não está emprestado!'
        else:
            data = self.data_emprestimo + timedelta(days=7)
            return f'Data do Emprestimo: {self.data_emprestimo_formatado} | Data de Devolução: {data}'

    def info_livro(self):
        ''' Exibe as informações do livro'''
        disponibilidade = 'Disponivel :)' if self.disponivel == True else 'Não Disponivel :('
        return f'Titulo: {self.titulo_formatado} | Autor: {self.autor_formatado} | Ano de Publicação: {self.ano_publicacao} | Disponibilidade: {disponibilidade}'
    
    def info_cliente(self):
        return f'Cliente: {self.nome_cliente_formatado} | CPF: {self.cpf_cliente_formatado}'

    @staticmethod
    def gerar_codigo():
        ''' Gera o codigo do livro '''
        return random.randint(10000, 100000)

    def adiciona_livro_na_biblioteca(self):
        ''' Tenho que adicionar corretamente as informações do livro no dicionario livro '''
        self.codigo_livro = self.gerar_codigo()
        self.disponivel = True
        self.livros = {
            'codigo': self.codigo_livro,
            'titulo': self.titulo,
            'autor': self.autor,
            'disponivel': self.disponivel
        }

        return f'Livro: {self.titulo} | Código do Livro: {self.codigo_livro} -> Adicionando à biblioteca'

    @classmethod
    def adiciona_cliente_ao_sistema(cls, cliente):
        cls.clientes.append(cliente)
        return f'Nome do Cliente: {cliente.nome_cliente} | CPF: {cliente.cpf_cliente} -> Cadastrado no sistema'


    @classmethod # Metodo estatico, permite acessar os atributos da classe sem precisar instanciá-la.
    def exibe_biblioteca(cls):
        ''' Retorna as informações de todos os livros da biblioteca '''
        if not cls.livros:
            return 'A biblioteca está vazia :('
        
        for codigo, info in cls.livros.items():
            disponibilidade = 'Disponível' if info['disponivel'] else 'Não Disponível'
            return f"Código: {codigo} | Título: {info['titulo']} | Autor: {info['autor']} | Disponibilidade: {disponibilidade}"

    # @classmethod 
    # def lista_clientes(cls, cliente):
    #     ''' Retorna as informações de todos os clientes do sistema '''
    #     if cls.cliente not in cls.clientes:
    #         raise ValueError(f'O cliente não esta cadastrado no sistema!')
    #     else:
    #         for cliente in cls.clientes:
    #             print(cliente.info_cliente())
