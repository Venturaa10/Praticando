import requests 
# r = requests.get('https://viacep.com.br/ws/01001000/json/')
cep = input('CEP: ')

if len(cep) == 8:
        busca_cep = f"https://viacep.com.br/ws/{cep}/json/"
        r = requests.get(busca_cep)
        dados = r.json()
        print('Endereço do Cliente')
        print(f'''
            CEP: {r.json()['cep']}
            Logradouro: {r.json()['logradouro']}
            Bairro: {r.json()['bairro']}
            Estado: {r.json()['uf']}
            DDD: {r.json()['ddd']}
    ''')
        
else:
    print(f'Tamanho inválido!')