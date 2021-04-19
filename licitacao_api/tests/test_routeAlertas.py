import json
from django.contrib.auth.models import User 
from rest_framework import status
from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework.reverse import reverse
from clientes.models import *
from contrib.models import *
from licitacoes.models import *
from clientes.serializers import *
from contrib.serializers import *
from licitacoes.serializers import *

class TestAlerta(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.regular_user = User.objects.create_user(username='testeuser1', email="testuser1@example.com", password="1234")
        self.super_user = User.objects.create_superuser(username='supertestuser1', email="supertestuser1@example.com", password="1234")
        self.clienteLicita = Cliente.objects.create(nomeCliente="Nome", CPNJ="333.333.333/0001-12", uasg="25635", cidade="Natal", estado="RN", pais="BR", observacao="Obs")
        self.tecnologiaLicita = [Tecnologia.objects.create(descricao="Teste de Tecnologia")]
        self.licitacaoLicita = Licitacao.objects.create(clienteGerenciadorID=self.clienteLicita, clienteBeneficiadoID=self.clienteLicita, modalidadeLicitacao="Pregão", tipoPregao="Eletrônico", numLicitacao="11111", registroPreco=True, objeto="Objeto", valorEstimado=234234, observacoes="asdasdas", statusLicitacao="Publicada", statusInterjato="Em analise" )
        self.licitacaoLicita.tecnologiaId.add(1)
        self.meioLicita = MeioEnvio.objects.create(descricao="email")
        self.tec = Alerta.objects.create(descricao="Alerta", licitacaoId=self.licitacaoLicita, destinatario="João", meioEnvioId=self.meioLicita)

        self.valid_payload = { "descricao": "Alerta 2",
                               "licitacaoId": 1,
                               "destinatario": "João",
                               "meioEnvioId": 1 }
        self.url = reverse('alerta-list')

    def _super_auth(self):
        self.client.force_authenticate(user=self.super_user)

    def _regular_auth(self):
        self.client.force_authenticate(user=self.regular_user)

class TestAlertaPost(TestAlerta):
    def test_create_valid_alerta(self):
        self._super_auth()
        response = self.client.post(
            reverse('alerta-list'),
            data=json.dumps(self.valid_payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

class TestAlertaGet(TestAlerta):
    def test_authorized_get_alerta(self):
        self._super_auth()
        response = self.client.get(self.url)
        expected_data = AlertaSerializer(Alerta.objects.all(), many=True).data
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, expected_data)
        self.assertEqual(Alerta.objects.count(), 1)


    def test_unauthorized_get_alerta(self):
        response = self.client.get(self.url, format='json')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

class TestAlertaPut(TestAlerta):
    def test_update_valid_alerta(self):
        self._super_auth()
        response = self.client.put(
            reverse('alerta-detail', kwargs={'pk': self.tec.pk}),
            data=json.dumps(self.valid_payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        response2 = self.client.get(
            reverse('alerta-detail', kwargs={'pk': self.tec.pk}))
        self.assertEqual(response2.data['descricao'], self.valid_payload['descricao'])

class TesteTipoDelete(TestAlerta):
    def test_delete_valid_alerta(self):
        self._super_auth()
        response = self.client.delete(
            reverse('alerta-detail', kwargs={'pk': self.tec.pk}))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        response2 = self.client.get(
            reverse('alerta-detail', kwargs={'pk': self.tec.pk}))
        self.assertEqual(response2.status_code, status.HTTP_404_NOT_FOUND)





