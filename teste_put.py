import requests

headers = {'Authorization': 'Token fb5fa62a417d8cc9f62e4500be6274d6ecf7ca1c'}

url_base_cursos = 'http://127.0.0.1:8000/api/v2/cursos/'
url_base_avaliacoes = 'http://127.0.0.1:8000/api/v2/avaliacoes/'

curso_atualizado = {
    "titulo": "Novo Curso de Scrum 8",
    "url": "http://www.geekuniversity.com.br/ncs8"
}
# Buscando o curso com ID 6
curso = requests.get(f'{url_base_cursos}6/', headers=headers)
print(curso)
print(curso.json())

resultado = requests.put(url=f'{url_base_cursos}6/', headers=headers, data=curso_atualizado)
print(resultado)
print(resultado.json())

# Testando o código de status HTTP
assert resultado.status_code == 200

# Testando o título
assert resultado.json()['titulo'] == curso_atualizado['titulo']
