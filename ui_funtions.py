import requests
import json

def consulta_cpf(cpf):
    url = f"https://www.sintegraws.com.br/api/v1/execute-api.php"
    querystring = {
        "token": "D8B77D55-D1CB-46DA-8F44-4A8F810D1A98",
        "cpf": cpf,
        "data-nascimento": "10111984",
        "plugin": "CPF"
    }
    response = requests.get(url, params=querystring)
    resp = json.loads(response.text)
    return (
        resp['nome'],
        resp['logradouro'],
        resp['numero'],
        resp['complemento'],
        resp['bairro'],
        resp['municipio'],
        resp['uf'],
        resp['cep'],
        resp['telefone'],
        resp['email']
    )

    
    
