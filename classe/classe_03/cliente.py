from validate_docbr import CPF
from biblioteca import Biblioteca
import re

class Cliente(Biblioteca):
    def __init__(self, nome_cliente: str, cpf_cliente:str):
        limpa_cpf = re.sub(r'[^a-zA-Z0-9]', '', cpf_cliente) # Remove todos os simbolos e espaços em brancos
        cpf_cliente = limpa_cpf 

        if not len(cpf_cliente) == 11:
            raise ValueError('CPF não está conforme esperado, verificar!')
        
        elif not isinstance(nome_cliente, str):
            raise ValueError('Nome do cliente invalido!')

        self.nome_cliente = nome_cliente
        self.cpf_cliente = self.valida(cpf_cliente)

    @property
    def nome_cliente_formatado(self):
        return self.nome_cliente.title()

    @property
    def cpf_cliente_formatado(self):
        mascara = CPF()
        return mascara.mask(self.cpf_cliente)

    def valida(self, cpf):
        validador = CPF()
        if validador.validate(cpf):
            print(f'CPF: {cpf} é valido!')
            return cpf
        else: 
            raise ValueError("cpf inválido!")

    def __str__(self):
        return f'Cliente: {self.nome_cliente_formatado} | CPF: {self.cpf_cliente_formatado}'
    
