import requests

def consultar_cep(cep):
  url = f'https://viacep.com.br/ws/{cep}/json/'

  r = requests.get(url)
  if (r.status_code == 200):
      print(
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
  else:
    condition = False

consultar_cep(input_cep)
