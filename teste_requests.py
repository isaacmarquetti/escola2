import requests


# GET Avaliações

avaliacoes = requests.get('http://127.0.0.1:8000/api/v2/avaliacoes/')

# Acessando o código de status HTTP
print(avaliacoes.status_code)

# Acessando os dados da resposta
print(avaliacoes.json())
print(type(avaliacoes.json()))

# Acessando a quantidade de registros
print(avaliacoes.json()['count'])

# Acessando a próxima página
print(avaliacoes.json()['next'])

# Acessando os resultados
print(avaliacoes.json()['results'])
print(type(avaliacoes.json()['results']))

# Acessando o primeiro elemento da lista de resultados
print(avaliacoes.json()['results'][0])

# Acessando somente o nome da pessoa que fez a última avaliação
print(avaliacoes.json()['results'][-1]['nome'])


# GET Avaliação

avaliacao = requests.get('http://127.0.0.1:8000/api/v2/avaliacoes/7/')

print(avaliacao.json())


# GET Cursos

headers = {'Authorization': 'Token fb5fa62a417d8cc9f62e4500be6274d6ecf7ca1c'}

cursos = requests.get(url='http://127.0.0.1:8000/api/v2/cursos/', headers=headers)
print(cursos.status_code)
print(cursos.json())
