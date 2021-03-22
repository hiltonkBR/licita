from django.test import TestCase
from clientes.models import *
from contrib.models import *
from licitacoes.models import *

class TecnologiaTestCase(TestCase):
    def test_str(self):
        """Test for string representation."""
        tecnologia = Tecnologia.objects.create(descricao="tecnologia")
        self.assertEqual(str(tecnologia), "tecnologia")

class TipoTestCase(TestCase):
    def test_str(self):
        """Test for string representation."""
        tipo = Tipo.objects.create(descricao="tipo")
        self.assertEqual(str(tipo), "tipo")

class EnvioTestCase(TestCase):
    def test_str(self):
        """Test for string representation."""
        envio = MeioEnvio.objects.create(descricao="envio")
        self.assertEqual(str(envio), "envio")