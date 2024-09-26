import requests
import re

def consultar_cep(cep):
  url = f'https://viacep.com.br/ws/{cep}/json/'

  r = requests.get(url)
  if (r.status_code == 200):
      print(
            f'\n'
            f'Cep: {r.json()["cep"]} \n'
            f'Rua: {r.json()["logradouro"]} \n'
            f'Bairro: {r.json()["bairro"]} \n'   
            f'Cidade: {r.json()["localidade"]} \n'
            f'Estado: {r.json()["estado"]} ({r.json()["uf"]})'
            )
  else:
    if(r.status_code >= 400) and (r.status_code <= 499):
      print(f'{r.status_code} - Error related with client error responses')
    elif(r.status_code >= 500) and (r.status_code <= 599):
      print(f'{r.status_code} - Error related with server error responses')
    else:
      print(f'Error: {r.status_code}')

################################################################################
################################################################################

print(f'-------------Consultador de CEP-------------')

condition = False

while(condition == False):
  input_cep = input("Digite o CEP:")
  if(len(input_cep) == 8):
    condition = True
  elif (len(input_cep) == 9) and (re.search(r'[-]',input_cep)):
    cep_split = input_cep.split("-")
    input_cep = cep_split[0]+cep_split[1]
    condition = True
  else:
    print(
          f'Alguma coisa está errada... \n'
          f'Tente digitar somente números. \n'
          f'Por exemplo: 32671674'
          )
    condition = False

consultar_cep(input_cep)
