import requests

headers = {'Authorization': 'Token 060903391a505e995dd1fccfad905776a5fcbea0'}

url_base_cursos = 'http://127.0.0.1:8000/api/v2/cursos/'
url_base_avaliacoes = 'http://127.0.0.1:8000/api/v2/avaliacoes/'

resultado = requests.delete(url=f'{url_base_cursos}6/', headers=headers)

print(resultado)
print(resultado.json())

# Testando o código HTTP de DELETE (204)
assert resultado.status_code == 204

# Testando se o tamanho do conteúdo retornado é 0
assert len(resultado.text) == 0
