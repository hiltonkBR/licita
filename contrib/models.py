from django.db import models

# Create your models here.
class Tecnologia (models.Model):
    class Meta:
        verbose_name = "Tecnologia "
        verbose_name_plural = "Tecnologias"

    def __str__(self):
        return self.descricao

    descricao = models.CharField(verbose_name="Descrição", max_length=200)
    dataCriacao = models.DateField(auto_now_add=True)
    dataEdicao = models.DateField(auto_now=True)

class Tipo (models.Model):
    class Meta:
        verbose_name = "Tipo de documento "
        verbose_name_plural = "Tipos de documentos"

    def __str__(self):
        return self.descricao

    descricao = models.CharField(verbose_name="Descrição", max_length=200)
    dataCriacao = models.DateField(auto_now_add=True)
    dataEdicao = models.DateField(auto_now=True)

class MeioEnvio (models.Model):
    class Meta:
        verbose_name = "Meio de envio "
        verbose_name_plural = "Meios de envio"

    def __str__(self):
        return self.descricao

    descricao = models.CharField(verbose_name="Descrição", max_length=200)
    dataCriacao = models.DateField(auto_now_add=True)
    dataEdicao = models.DateField(auto_now=True)