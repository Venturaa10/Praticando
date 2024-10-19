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

        else:
            pass
        
        self._titulo = titulo
        self._autor = autor
        self._ano_publicacao = ano_publicacao
        self._disponivel = None
        self._codigo_livro = None
        self._data_emprestimo = None

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
        return 'Disponivel :)' if self._disponivel == True else 'Não Disponivel :('

    @property 
    def codigo_livro(self):
        return 'N/A' if self._codigo_livro == None else self._codigo_livro
    
    @property
    def data_emprestimo(self):
        ''' Formata a data para o padrão do Brasil '''
        return 'Sem data definida no momento!' if self._data_emprestimo == None else self._data_emprestimo.strftime('%d/%m/%Y')
    
    def __str__(self):
        return f'Autor: {self.autor} | Titulo: {self.titulo} | Ano: {self.ano_publicacao}'

