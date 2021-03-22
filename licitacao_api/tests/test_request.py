from django.test import TestCase
from clientes.models import *
from contrib.models import *
from licitacoes.models import *

class TestTecnologias(TestCase):
    def test_can_send_message(self):
        data = {
            "descricao": "descricao test"
        }
        response = self.client.post("/tecnologias", data=data)
        self.assertEqual(Tecnologia.objects.count(), 0)