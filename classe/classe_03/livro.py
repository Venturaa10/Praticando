import random
from datetime import datetime, timedelta
from biblioteca import Biblioteca

class Livro(Biblioteca):
    def __init__(self, titulo: str, autor: str, ano_publicacao: int):      
            # if not -> Se não existir valor ou condição for falsa
        if not isinstance(titulo, str) or not titulo.strip():
            raise ValueError('Titulo Invalido!')
        
        elif not isinstance(autor, str) or not autor.strip():
            raise ValueError('Nome do autor invalido!')
        
        elif not isinstance(ano_publicacao, int):
            raise ValueError('Ano Invalido!')
        
        self._titulo = titulo
        self._autor = autor
        self._ano_publicacao = ano_publicacao
        self._disponivel = False
        self._codigo_livro = False
        self._data_emprestimo = False


    def __str__(self):
        return f'Autor: {self.autor} | Titulo: {self.titulo} | Ano: {self.ano_publicacao}'

    @property
    def titulo(self):
        return self._titulo.title()

    @property
    def autor(self):
        return self._autor.title()
    
    @property
    def ano_publicacao(self):
        return self._ano_publicacao
    
    @property
    def disponivel(self):
        return f'Disponivel :)' if self._disponivel else 'Não Disponivel :('

    @property 
    def codigo_livro(self):
        return 'N/A' if self._codigo_livro == False else self._codigo_livro

    @property
    def data_emprestimo(self):
        ''' Formata a data para o padrão do Brasil '''
        if self._data_emprestimo:
            return self._data_emprestimo.strftime('%d/%m/%Y')
        else:
            return f'O livro código: {self.codigo_livro} não esta emprestado!'
    
    @data_emprestimo.setter
    def data_emprestimo(self, data):
        ''' Define a data de empréstimo como um objeto datetime '''
        self._data_emprestimo = datetime.strptime(data, '%d/%m/%Y')


