import os 
from datetime import datetime, timedelta
os.system('cls')

class Biblioteca:
    livros = []
    def __init__(self):
        # Atributos da classe Biblioteca
        self.disponivel = True
        self.data_emprestimo = None
        Biblioteca.livros.append(self) # Adiciona o objeto criado dentro da biblioteca

    @property
    def data_emprestimo_formatado(self):
        ''' Formata a data para o padrão do Brasil '''
        if self.disponivel:
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

    def informacoes(self):
        ''' Exibe as informações do livro'''
        disponibilidade = 'Disponivel :)' if self.disponivel == True else 'Não Disponivel :('
        return f'Titulo: {self.titulo_formatado} | Autor: {self.autor_formatado} | Ano de Publicação: {self.ano_publicacao} | Disponibilidade: {disponibilidade}'


    @classmethod # Metodo estatico, permite acessar os atributos da classe sem precisar instanciá-la.
    def exibe_biblioteca(cls):
        ''' Retorna as informações de todos os livros da biblioteca '''
        if not cls.livros:
            return f'A biblioteca está vazia :('
        
        else:
            for livro in cls.livros:
                print(livro.informacoes())


