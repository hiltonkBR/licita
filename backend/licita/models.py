from django.db import models

# Create your models here.

class Licitacoes(models.Model):
    orgao = models.CharField(max_length=250)
    tecnologia = models.CharField(max_length=250)
    valor = models.CharField(max_length=100)

    def _str_(self):
        return self.orgao
