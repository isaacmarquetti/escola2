import requests


class TestCursos:
    headers = {'Authorization': 'Token 060903391a505e995dd1fccfad905776a5fcbea0'}
    url_base_cursos = 'http://127.0.0.1:8000/api/v2/cursos/'

    def test_get_cursos(self):
        cursos = requests.get(url=self.url_base_cursos, headers=self.headers)

        assert cursos.status_code == 200

    def test_get_curso(self):
        resposta = requests.get(url=f'{self.url_base_cursos}/5', headers=self.headers)

        assert resposta.status_code == 200

    def test_post_curso(self):
        novo = {
            "titulo": "Curso de Programação com Ruby",
            "url": "http://www.geekuniversity.com.br/cpr"
        }
        resposta = requests.post(url=self.url_base_cursos, headers=self.headers, data=novo)

        assert resposta.status_code == 201
        assert resposta.json()['titulo'] == novo['titulo']

    def test_put_curso(self):
        atualizado = {
            "titulo": "Novo curso de Ruby",
            "url": "http://www.geekuniversity.com.br/novocpr"
        }

        resposta = requests.put(url=f'{self.url_base_cursos}3/', headers=self.headers, data=atualizado)

        assert resposta.status_code == 200

    def test_put_titulo_curso(self):
        atualizado = {
            "titulo": "Novo curso de Ruby 2",
            "url": "http://www.geekuniversity.com.br/novocpr2"
        }

        resposta = requests.put(url=f'{self.url_base_cursos}3/', headers=self.headers, data=atualizado)

        assert resposta.json()['titulo'] == atualizado['titulo']

    def test_delete_curso(self):
        resposta = requests.delete(url=f'{self.url_base_cursos}3/', headers=self.headers)

        assert resposta.status_code == 204 and len(resposta.text) == 0
