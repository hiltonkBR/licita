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

class TestTecnologias(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.regular_user = User.objects.create_user(username='testeuser1', email="testuser1@example.com", password="1234")
        self.super_user = User.objects.create_superuser(username='supertestuser1', email="supertestuser1@example.com", password="1234")
        self.tec = Tecnologia.objects.create(descricao="Teste de Tecnologia")
        self.valid_payload = {'descricao' : 'Nova tecnologia'}
        self.url = reverse('tecnologia-list')

    def _super_auth(self):
        self.client.force_authenticate(user=self.super_user)

    def _regular_auth(self):
        self.client.force_authenticate(user=self.regular_user)

class TestTecnologiaPost(TestTecnologias):
    def test_create_valid_tecnologia(self):
        self._super_auth()
        response = self.client.post(
            reverse('tecnologia-list'),
            data=json.dumps(self.valid_payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

class TestTecnologiaGet(TestTecnologias):
    def test_authorized_get_Tecnologia(self):
        self._super_auth()
        response = self.client.get(self.url)
        expected_data = TecnologiaSerializer(Tecnologia.objects.all(), many=True).data
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, expected_data)
        self.assertEqual(Tecnologia.objects.count(), 1)


    def test_unauthorized_get_Tecnologia(self):
        response = self.client.get(self.url, format='json')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

class TestTecnologiaPut(TestTecnologias):
    def test_update_valid_tecnologia(self):
        self._super_auth()
        response = self.client.put(
            reverse('tecnologia-detail', kwargs={'pk': self.tec.pk}),
            data=json.dumps(self.valid_payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        response2 = self.client.get(
            reverse('tecnologia-detail', kwargs={'pk': self.tec.pk}))
        self.assertEqual(response2.data['descricao'], self.valid_payload['descricao'])

class TesteTecnologiaDelete(TestTecnologias):
    def test_delete_valid_tecnologia(self):
        self._super_auth()
        response = self.client.delete(
            reverse('tecnologia-detail', kwargs={'pk': self.tec.pk}))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        response2 = self.client.get(
            reverse('tecnologia-detail', kwargs={'pk': self.tec.pk}))
        self.assertEqual(response2.status_code, status.HTTP_404_NOT_FOUND)



