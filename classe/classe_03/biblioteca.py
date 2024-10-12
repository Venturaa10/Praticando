import os 
os.system('cls')

class Livro:
    def __init__(self, titulo, autor, ano_publicacao):
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
        self.disponivel = True

    def emprestar(self):
        if self.disponivel == True:
            self.disponivel = False
            return f'Livro "{self.titulo}" emprestado, tenha uma otima leitura :)'
        else:
            return f'O livro "{self.titulo}" não está disponivel!'

    def devolver(self):
        if self.disponivel == True:
            return f'Não é possivel fazer a devolução, o livro não foi emprestado!'
        else:    
            self.disponivel = True
            return f'Livro "{self.titulo}" devolvido a biblioteca!'        

    def informacoes(self):
        disponibilidade = 'Disponivel :)' if self.disponivel == True else 'Não Disponivel :('
        return f'Titulo: {self.titulo} | Autor: {self.autor} | Ano de Publicação: {self.ano_publicacao} | Disponibilidade: {disponibilidade}'

