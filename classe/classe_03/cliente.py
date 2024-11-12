from validate_docbr import CPF
from biblioteca import Biblioteca
import re

class Cliente(Biblioteca):
    def __init__(self, nome_cliente: str, cpf_cliente:str, email_cliente:str):
        limpa_cpf = re.sub(r'[^a-zA-Z0-9]', '', cpf_cliente) # Remove todos os simbolos e espaços em brancos
        cpf_cliente = limpa_cpf 
        email_regex = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'

        if not len(cpf_cliente) == 11:
            raise ValueError('CPF não está conforme esperado, verificar!')
        
        if not isinstance(nome_cliente, str):
            raise ValueError('Nome do cliente invalido!')

        if re.match(email_regex, email_cliente.strip(' ')) == None:
            raise ValueError(f'Email invalido: {email_cliente}')

        self._nome_cliente = nome_cliente
        self._cpf_cliente = self.valida(cpf_cliente)
        self._email_cliente = email_cliente

    def __str__(self):
        return f'Cliente: {self.nome_cliente} | CPF: {self.cpf_cliente} | Email: {self.email_cliente}'
    
    @property
    def nome_cliente(self):
        return self._nome_cliente.title()

    @property
    def cpf_cliente(self):
        mascara = CPF()
        return mascara.mask(self._cpf_cliente)

    @property
    def email_cliente(self):
        return self._email_cliente.strip(' ')

    def valida(self, cpf):
        validador = CPF()
        if validador.validate(cpf):
            print(f'CPF: {cpf} é valido!')
            return cpf
        else: 
            raise ValueError("cpf inválido!")

    
