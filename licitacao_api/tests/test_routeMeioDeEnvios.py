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

class TestMeioEnvio(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.regular_user = User.objects.create_user(username='testeuser1', email="testuser1@example.com", password="1234")
        self.super_user = User.objects.create_superuser(username='supertestuser1', email="supertestuser1@example.com", password="1234")
        self.tec = MeioEnvio.objects.create(descricao="Tipo")
        self.valid_payload = {'descricao' : 'Video Monitoramento'}
        self.url = reverse('meioenvio-list')

    def _super_auth(self):
        self.client.force_authenticate(user=self.super_user)

    def _regular_auth(self):
        self.client.force_authenticate(user=self.regular_user)

class TestMeioEnvioPost(TestMeioEnvio):
    def test_create_valid_meioEnvio(self):
        self._super_auth()
        response = self.client.post(
            reverse('meioenvio-list'),
            data=json.dumps(self.valid_payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

class TestMeioEnvioGet(TestMeioEnvio):
    def test_authorized_get_meioEnvio(self):
        self._super_auth()
        response = self.client.get(self.url)
        expected_data = MeioEnvioSerializer(MeioEnvio.objects.all(), many=True).data
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, expected_data)
        self.assertEqual(MeioEnvio.objects.count(), 1)


    def test_unauthorized_get_meioEnvio(self):
        response = self.client.get(self.url, format='json')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

class TestMeioEnvioPut(TestMeioEnvio):
    def test_update_valid_meioEnvio(self):
        self._super_auth()
        response = self.client.put(
            reverse('meioenvio-detail', kwargs={'pk': self.tec.pk}),
            data=json.dumps(self.valid_payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        response2 = self.client.get(
            reverse('meioenvio-detail', kwargs={'pk': self.tec.pk}))
        self.assertEqual(response2.data['descricao'], self.valid_payload['descricao'])

class TesteTipoDelete(TestMeioEnvio):
    def test_delete_valid_meioEnvio(self):
        self._super_auth()
        response = self.client.delete(
            reverse('meioenvio-detail', kwargs={'pk': self.tec.pk}))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        response2 = self.client.get(
            reverse('meioenvio-detail', kwargs={'pk': self.tec.pk}))
        self.assertEqual(response2.status_code, status.HTTP_404_NOT_FOUND)






