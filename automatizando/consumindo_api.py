import requests

print('##################')
print('###Consulta CEP###')
print('##################')
print()

cep_input = input('Digite o CEP para consulta: ')

if len(cep_input) != 8:
    print('Quantidade do CEP INCORRETA!')
    exit()

request = requests.get(f'https://viacep.com.br/ws/{cep_input}/json/')
#print(request.json())

address_data = request.json()

if 'erro' not in address_data:
    print(address_data)
else:
    print('CEP inválido')
