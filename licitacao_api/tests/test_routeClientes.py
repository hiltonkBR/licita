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

class TestClientes(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.regular_user = User.objects.create_user(username='testeuser1', email="testuser1@example.com", password="1234")
        self.super_user = User.objects.create_superuser(username='supertestuser1', email="supertestuser1@example.com", password="1234")
        self.tec = Cliente.objects.create(nomeCliente="Nome", CPNJ="333.333.333/0001-12", uasg="25635", cidade="Natal", estado="RN", pais="BR", observacao="Obs")
        self.valid_payload = {'nomeCliente' : 'Nome2',
                              'CPNJ' : '333.333.333/0001-12',
                              'uasg' : '345345',
                              'cidade' : 'Natal',
                              'estado' : 'RN',
                              'pais' : 'BR',
                              'observacao' : 'Obs'}
        self.url = reverse('clientes-list')

    def _super_auth(self):
        self.client.force_authenticate(user=self.super_user)

    def _regular_auth(self):
        self.client.force_authenticate(user=self.regular_user)

class TestClientesPost(TestClientes):
    def test_create_valid_clientes(self):
        self._super_auth()
        response = self.client.post(
            reverse('clientes-list'),
            data=json.dumps(self.valid_payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

class TestClientesGet(TestClientes):
    def test_authorized_get_clientes(self):
        self._super_auth()
        response = self.client.get(self.url)
        expected_data = ClienteSerializer(Cliente.objects.all(), many=True).data
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, expected_data)
        self.assertEqual(Cliente.objects.count(), 1)


    def test_unauthorized_get_clientes(self):
        response = self.client.get(self.url, format='json')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

class TestClientesPut(TestClientes):
    def test_update_valid_clientes(self):
        self._super_auth()
        response = self.client.put(
            reverse('clientes-detail', kwargs={'pk': self.tec.pk}),
            data=json.dumps(self.valid_payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        response2 = self.client.get(
            reverse('clientes-detail', kwargs={'pk': self.tec.pk}))
        self.assertEqual(response2.data['nomeCliente'], self.valid_payload['nomeCliente'])

class TesteTipoDelete(TestClientes):
    def test_delete_valid_clientes(self):
        self._super_auth()
        response = self.client.delete(
            reverse('clientes-detail', kwargs={'pk': self.tec.pk}))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        response2 = self.client.get(
            reverse('clientes-detail', kwargs={'pk': self.tec.pk}))
        self.assertEqual(response2.status_code, status.HTTP_404_NOT_FOUND)





