from django.test import TestCase
from rest_framework.utils import json
from rest_framework.test import APIRequestFactory, APIClient
from feiraslivres.core.models import FeirasLivres



class ListaTest(TestCase):

    def setUp(self):
        self.lista = self.client.get('/feiraslivres/')
        self.distrito = self.client.get('/feiraslivres/distrito/jabaquara/')
        self.bairro = self.client.get('/feiraslivres/bairro/santana/')
        self.regiao5 = self.client.get('/feiraslivres/regiao5/leste/')
        self.nome_feira = self.client.get('/feiraslivres/nome_feira/aclimacao/')
        self.factory = APIRequestFactory()
        self.data_post = dict(
            nome_feira="FEIRA",
            registro="7777-7",
            bairro="BAIRRO",
            logradouro="LOGRADOURO",
            numero="S/N",
            referencia="REFERENCIA",
            lat=-23550464,
            long=-46659253,
            setcens=355030826000014,
            areap=3550308005013,
            coddist=26,
            distrito="DISTRITO",
            codsubpref=9,
            subprefe="SE",
            regiao5="Centro",
            regiao8="Centro"
        )

        self.data_put = dict(
            nome_feira="NOVA FEIRA",
            bairro="NOVO BAIRRO",
            logradouro="NOVO LOGRADOURO",
            numero="S/N",
            referencia="NOVA REFERENCIA",
            lat=0,
            long=0,
            setcens=0,
            areap=0,
            coddist=0,
            distrito="NOVO DISTRITO",
            codsubpref=0,
            subprefe="NOVA SUBPREFE",
            regiao5="SUL",
            regiao8="SUL"
        )

    def test_get_lista(self):
        self.assertEqual(self.lista.status_code, 200)

    def test_get_distrito(self):
        self.assertEqual(self.distrito.status_code, 200)

    def test_get_bairro(self):
        self.assertEqual(self.bairro.status_code, 200)

    def regiao5(self):
        self.assertEqual(self.regiao5.status_code, 200)

    def test_get_nome_feira(self):
        self.assertEqual(self.nome_feira.status_code, 200)

    def test_post(self):
        """ Cadastra uma nova feira """
        resp = self.factory.post('/feiraslivres/', json.dumps(self.data_post), format='json')
        self.assertEqual(resp.content_type, 'application/json')
        self.assertTrue(FeirasLivres.objects.filter(registro='7777-7').exists())

    def test_put(self):
        """ Altera dados de uma feira """
        resp = self.factory.put('/feiralivre/7777-7/', json.dumps(self.data_put), format='json')
        self.assertEqual(resp.content_type, 'application/json')

    def test_delete(self):
        """ Deleta uma feira """
        resp = self.factory.delete('/feiralivre/7777-7/')
        self.assertTrue(FeirasLivres.objects.filter(registro='7777-7').exists())