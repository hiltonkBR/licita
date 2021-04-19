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

class TestComentario(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.regular_user = User.objects.create_user(username='testeuser1', email="testuser1@example.com", password="1234")
        self.super_user = User.objects.create_superuser(username='supertestuser1', email="supertestuser1@example.com", password="1234")
        self.clienteLicita = Cliente.objects.create(nomeCliente="Nome", CPNJ="333.333.333/0001-12", uasg="25635", cidade="Natal", estado="RN", pais="BR", observacao="Obs")
        self.tecnologiaLicita = [Tecnologia.objects.create(descricao="Teste de Tecnologia")]
        self.licita = Licitacao.objects.create(clienteGerenciadorID=self.clienteLicita, clienteBeneficiadoID=self.clienteLicita, modalidadeLicitacao="Pregão", tipoPregao="Eletrônico", numLicitacao="11111", registroPreco=True, objeto="Objeto", valorEstimado=234234, observacoes="asdasdas", statusLicitacao="Publicada", statusInterjato="Em analise" )
        self.licita.tecnologiaId.add(1)
        self.tec = Comentario.objects.create(autor="Hilton", comentario="Comentario", criticidade="1", licitacaoId=self.licita)
        self.valid_payload = { "autor": "João",
                               "comentario": "New COmment",
                               "modalidadeLicitacao": "Pregão",
                               "criticidade": "1",
                               "licitacaoId": 1 }

        self.url = reverse('comentario-list')

    def _super_auth(self):
        self.client.force_authenticate(user=self.super_user)

    def _regular_auth(self):
        self.client.force_authenticate(user=self.regular_user)

class TestComentarioPost(TestComentario):
    def test_create_valid_comentario(self):
        self._super_auth()
        response = self.client.post(
            reverse('comentario-list'),
            data=json.dumps(self.valid_payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

class TestComentarioGet(TestComentario):
    def test_authorized_get_comentario(self):
        self._super_auth()
        response = self.client.get(self.url)
        expected_data = ComentarioSerializer(Comentario.objects.all(), many=True).data
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, expected_data)
        self.assertEqual(Comentario.objects.count(), 1)


    def test_unauthorized_get_comentario(self):
        response = self.client.get(self.url, format='json')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

class TestComentarioPut(TestComentario):
    def test_update_valid_comentario(self):
        self._super_auth()
        response = self.client.put(
            reverse('comentario-detail', kwargs={'pk': self.tec.pk}),
            data=json.dumps(self.valid_payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        response2 = self.client.get(
            reverse('comentario-detail', kwargs={'pk': self.tec.pk}))
        self.assertEqual(response2.data['autor'], self.valid_payload['autor'])

class TesteTipoDelete(TestComentario):
    def test_delete_valid_comentario(self):
        self._super_auth()
        response = self.client.delete(
            reverse('comentario-detail', kwargs={'pk': self.tec.pk}))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        response2 = self.client.get(
            reverse('comentario-detail', kwargs={'pk': self.tec.pk}))
        self.assertEqual(response2.status_code, status.HTTP_404_NOT_FOUND)





