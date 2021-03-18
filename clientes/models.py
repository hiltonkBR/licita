from django.db import models

class Cliente(models.Model):
    class Meta:
            verbose_name = "Cliente"
            verbose_name_plural = "Clientes"

    def __str__(self):
        return self.nomeCliente


    nomeCliente = models.CharField(verbose_name="Nome do Cliente", max_length=150)
    CPNJ = models.CharField(verbose_name="", max_length=30)
    cidade = models.CharField(verbose_name="Cidade", max_length=150)
    estado = models.CharField(verbose_name="Estado", max_length=50)
    pais = models.CharField(verbose_name="Pais", max_length=50)
    nomeContato = models.CharField(verbose_name="Nome do Contato", max_length=150, null=True)
    telefoneContato = models.CharField(verbose_name="Telefone do Contato", max_length=50, null=True)
    observacao = models.TextField(verbose_name="Observações", null=True)
    dataCrialcao = models.DateField(auto_now_add=True)
    dataEdicao = models.DateField(auto_now=True)
