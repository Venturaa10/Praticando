import os 
os.system('cls')

class Livro:
    def __init__(self, titulo, autor, ano_publicacao):
        self.titulo = titulo
        self.autor = autor
        self.ano_publicacao = ano_publicacao
        self.disponivel = True

    def emprestar(self):
        if self.disponivel == True:
            self.disponivel = False
            return f'Livro "{self.livro}" emprestado, tenha uma otima leitura :)'
        else:
            return f'O livro "{self.titulo}" não está disponivel!'

    def devolver(self):
        self.disponivel = True
        return f'Livro "{self.titulo}" devolvido a biblioteca!'        
    
    def informacoes(self):
        disponibilidade = 'Disponivel :)' if self.disponivel == True else 'Não Disponivel :('
        return f'Titulo: {self.titulo} | Autor: {self.autor} | Ano de Publicação: {self.ano_publicacao} | Disponibilidade: {disponibilidade}'
    

if __name__ == "__main__":
    livro1 = Livro('Sherlock Holmes', 'Sherlock', 2000)
    print(livro1.emprestar())
    print(livro1.informacoes())
    print(livro1.emprestar())
    print(livro1.devolver())
    print(livro1.informacoes())

    livro2 = Livro('Bobos e Bocos', 'Alisson', 2010)
    print(livro2.emprestar())
    print(livro2.devolver())
    print(livro2.informacoes())
