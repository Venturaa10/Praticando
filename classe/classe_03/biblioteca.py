import os 
import random
from validate_docbr import CPF
from datetime import datetime, timedelta

os.system('cls')

class Biblioteca:
    livros = {}
    clientes = {}

    @classmethod # Metodo estatico, permite acessar os atributos da classe sem precisar instanciá-la.
    def exibe_biblioteca(cls):
        ''' 
        Método responsavel por exibir todos os livros cadastrados no sistema, se houver pelo menos um livro no sistema.\n
        -> Se não, retorna uma mensagem informando que a biblioteca está vazia.\n
        -> O "for" percorre os items do dicionario "livros" da classe.
        -> Pega os pares de chave e valor do dicionário cls.livros (onde a chave é o identificador do livro (O codigo do livro nesse caso) e o valor é outro dicionário contendo informações sobre o livro), e adiciona uma string formatada com os detalhes do livro na lista "livros_lista".\n
        -> Retorna os itens da lista utilizando o "join" para juntar os elementos da lista, porém o \n faz com que seja exibido um abaixo do outro.
         '''
        livros_lista = []

        print(cls.livros.items())
        if not cls.livros:
            return 'A biblioteca está vazia :('

        for livro, info in cls.livros.items():
            livros_lista.append(f"Código: {info['codigo']} | Título: {info['titulo']} | Autor: {info['autor']} | Disponibilidade: {info['disponivel']}")

        return '\n'.join(livros_lista) 


    @classmethod
    def exibe_clientes(cls):
        '''
        Método responsavel por exibir todos os clientes cadastrado no sistema.\n
        ->Verifica se há pelo menos um cliente dentro do dicionario "clientes", se não houver o retorno é uma mensagem informando que não há clientes.\n
        -> O for percorre os items do dicionario "clientes", e adiciona uma mensagem formatada dentro da lista "clientes_lista".
        '''
        clientes_lista = []
        if not cls.clientes:
            return 'Nenhum cliente encontrado no sistema!'

        for cliente, info in cls.clientes.items():
            clientes_lista.append(f"CPF: {info['cpf']} | Nome Completo: {info['nome']}")

        return '\n'.join(clientes_lista) # Une os itens da lista, porém o \n faz com que seja exibido um abaixo do outro.


    @property
    def data_devolucao(self):
        '''
        Método responsavel por exibir a data de devolução de algum livro.\n
        -> Verifica se o livro está cadastrado no sistema, em caso do livro cadastrado, verifica se o livro está disponivel para aluguel.\n
        -> Se true, retorna uma mensagem informando que o livro está disponivel para aluguel e consequentemente não possui data de devolução.\n
        -> Se não, a variavel "data_devolução" recebe uma data baseada na data do dia de emprestimo + 7 dias (representa os dias que o usuario fica com o livro).\n
        -> Retorna a data de devolução formatada para exibir no formato: 10/10/2020.\n
        '''
        if not self.verifica_livro_cadastro():
            if self._disponivel:
                return self.mensagem_livro_disponibilidade()
            else:
                data_devolucao = self._data_emprestimo + timedelta(days=7)
                return data_devolucao.strftime('%d/%m/%Y') 

            
    def verifica_livro_cadastro(self):
        '''
        Verifica se o atributo "_codigo_livro" é False, isso indica que o livro não foi cadastrado no sistema.
        Tornando possivel a execução de outros metodos apenas se o livro possuir um codigo.

        Retorna um "ValueError" informando que o livro não está cadastrado no sistema
        '''        
        if self._codigo_livro == False:
            raise ValueError('Não foi possivel realizar a operação, pois o livro ainda não foi cadastrado no sistema!')
        

    def gerar_codigo(self):
        ''' Gera o codigo do livro '''
        return random.randint(10000, 100000)
    

    def adiciona_livro_na_biblioteca(self):
        ''' Metodo responsavel por adicionar o livro no sistema.\n
        O livro quando adicionado no sistema, recebe:\n
        -> O livro recebe um codigo unico.\n
        -> O livro fica disponivel para emprestimo ao usuario.\n
        -> Um dicionario é gerado atraves do codigo do livro, e adicionado ao dicionario "livros".\n
        -> Dentro do dicionario gerado pelo livro, a informação do livro são armazenados dentro do dicionario em uma combinação de chave(nome_atributo):valor(self_atributo).\n
        -> Retorna uma mensagem informando o nome e o codigo do livro adicionado ao dicionario "livros".\n
        '''
        self._codigo_livro = self.gerar_codigo()
        self._disponivel = True
        Biblioteca.livros[self._codigo_livro] = { 
            'codigo': self.codigo_livro,
            'titulo': self.titulo,
            'autor': self.autor,
            'disponivel': self.disponivel,
        }
        return f'Livro: {self.titulo} | Código do Livro: {self.codigo_livro} -> Adicionando à biblioteca'


    def adiciona_cliente_ao_sistema(self):
        ''' Metodo responsavel por adicionar o cliente no sistema.\n
            -> Um dicionario é gerado atraves do "CPF" do cliente, dentro desse dicionario as informações são passados em uma combinação de chave:valor, as informações do cliente.\n
            -> Retorna uma mensagem informando o nome o CPF do cliente adicionado ao dicionario "clientes"\n
         '''
        Biblioteca.clientes[self.cpf_cliente] = {
            'nome': self.nome_cliente,
            'cpf': self.cpf_cliente
        }
        return f'Nome do Cliente: {self.nome_cliente} | CPF: {self.cpf_cliente} -> Cadastrado no sistema'


    def info_livro(self):
        ''' Método responsavel por exibir informações do livro '''
        if not self.verifica_livro_cadastro():
            if self._disponivel:
                return f'Código do Livro: {self.codigo_livro} | Titulo: {self.titulo} | Autor: {self.autor} | Ano de Publicação: {self.ano_publicacao} | Disponibilidade: {self.disponivel}'
            else:
                return f'Código do Livro: {self.codigo_livro} | Titulo: {self.titulo} | Autor: {self.autor} | Ano de Publicação: {self.ano_publicacao} | Disponibilidade: {self.disponivel} | Data de Devolução: {self.data_devolucao}'

        
    def info_cliente(self):
        ''' Método responsavel por exibir informações do cliente '''
        return f'Cliente: {self.nome_cliente} | CPF: {self.cpf_cliente}'


    def emprestar(self):
        ''' Método responsavel por realizar o emprestimo de um livro.\n
        Verificações e Validações:\n
        -> Se livro está cadastrado no sistema, se livro não cadastrado no sistema, retorna uma mensagem informando erro.\n
        -> Verifica se "_disponivel" é True, indicando que livro está disponivel para emprestimo.\n
        -> Se "_disponivel" True, o atributo "_disponivel" recebe "false" como valor, informando que agora o livro está emprestado.\n
        -> O atributo "_data_emprestimo" recebe um valor, esse valor é a data atual, que indica o dia que o livro foi emprestado.\n
        -> Retorna uma mensagem formatada, informando que o emprestimo foi realizado com sucesso.\n
        -> Em caso de livro não disponivel para aluguel, retorna uma mensagem através do método "mensagem_livro_disponibilidade" 
        '''
        if not self.verifica_livro_cadastro():
            if self._disponivel:
                self._disponivel = False
                self._data_emprestimo = datetime.today()
                return f'Livro "{self.titulo}" emprestado no dia {self.data_emprestimo}, tenha uma otima leitura :)'
            else:
                return self.mensagem_livro_disponibilidade()


    def verifica_data_devolucao(self):
        ''' Método responsavel pela consulta e exibição da data de devolução do livro.\n
        -> Verifica se livro está cadastrado no sistema\n
        -> Verifica se livro está disponivel para aluguel, consequentemente não é possivel ter uma data para devolução, e retorna uma mensagem através do método "mensagem_livro_disponibilidade".\n
        -> Em caso de "_disponivel" False, retorna uma mensagem personalizada informando a data de devolução do livro.
        '''
        if not self.verifica_livro_cadastro():
            if self._disponivel:
                return self.mensagem_livro_disponibilidade()
            else:
                return f'Data do Emprestimo: {self.data_emprestimo} | Data de Devolução: {self.data_devolucao}'


    def verifica_data_emprestimo(self):
        ''' Método responsavel pela consulta e exibição da data de emprestimo do livro.\n
        -> Verifica se livro esta cadastrado no sistema.\n
        -> Verifica se livro está alugado, através do valor do atributo "_disponivel", se True significa que o livro não está emprestado, e retorna uma mensagem personalizada através do método "_mensagem_livro_disponibilidade".\n
        -> Se não, retorna a data de emprestimo do livro.
        
        '''
        if not self.verifica_livro_cadastro():
            if self._disponivel:
                return self.mensagem_livro_disponibilidade()
            else:
                self._data_emprestimo = datetime.today().strftime('%d/%m/%Y')
                return f'Data emprestimo:{self._data_emprestimo}'
            

    def devolver(self):
        ''' Método responsavel por realizar a devolução de um livro que estava emprestado. 
        -> Verifica se livro está cadastrado no sistema.\n
        -> Verifica se livro está alugado, através do valor do atributo "_disponivel", se True significa que o livro não está emprestado, e retorna uma mensagem personalizada através do método "_mensagem_livro_disponibilidade".\n        
        -> Se não, o atributo "_disponivel" recebe o valor "true", indicando que agora está disponivel para emprestimo e retorna uma mensagem informando a devolução do livro.\n
        '''
        if not self.verifica_livro_cadastro():
            if self._disponivel:
                return self.mensagem_livro_disponibilidade()
            else:    
                self._disponivel = True
                return f'Livro "{self.titulo}" devolvido a biblioteca!'       
            
            
    def mensagem_livro_disponibilidade(self):
        ''' Método responsavel por exibir uma mensagem personalizada informando se o livro está disponivel para emprestimo ou não.\n
        -> Se "_disponivel" True, retorna mensagem indicando que livro está disponivel para emprestimo.\n
        -> Se não, retorna uma mensagem informando que o livro não está disponivel para emprestimo.
         '''
        if self._disponivel:
            return f'O livro "{self.titulo}" está disponivel!'
        else:
            return f'O livro "{self.titulo}" não está disponivel!'




    
