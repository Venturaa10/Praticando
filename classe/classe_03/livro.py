import random
from biblioteca import Biblioteca

class Livro(Biblioteca):
    def __init__(self, titulo, autor, ano_publicacao):      
            # if not -> Se não existir valor ou condição for falsa
        if not isinstance(titulo, str) or not titulo.strip():
            raise ValueError('Titulo Invalido!')
        
        elif not isinstance(autor, str) or not autor.strip():
            raise ValueError('Nome do autor invalido!')
        
        elif not isinstance(ano_publicacao, int):
            raise ValueError('Ano Invalido!')

        else:
            pass
        
        self.titulo = titulo
        self.autor = autor
        self.ano_publicacao = ano_publicacao
        self.disponivel = None

    @property
    def titulo_formatado(self):
        return self.titulo.title()

    @property
    def autor_formatado(self):
        return self.autor.title()
    
    
    def __str__(self):
        return f'Autor: {self.autor_formatado} | Titulo: {self.titulo_formatado} | Ano: {self.ano_publicacao}'

