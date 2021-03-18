from django.db import models
from contrib.models import Tecnologia, Tipo, MeioEnvio

class Licitacao (models.Model):
    class Meta:
        verbose_name = "Licitacão"
        verbose_name_plural = "Licitações"

    def __str__(self):
        return self.orgao

    choiceStatus = (
        ("Publicada", "Publicada"),
        ("Recolhida", "Recolhida"),
        ("Republicada", "Republicada"),
        ("Encerrada", "Encerrada")
    )

    orgao = models.CharField(verbose_name="Órgão licitante", max_length=200)
    pregao = models.IntegerField(verbose_name="Número do pregão")
    uasg = models.IntegerField(verbose_name="Número do UASG")
    descricao = models.CharField(verbose_name="Descrição", max_length=200)
    tecnologiaId = models.ManyToManyField(Tecnologia, verbose_name="Tecnologias")
    observacoes = models.TextField(verbose_name="Observações")
    status = models.CharField(verbose_name="Situação", max_length=11, choices=choiceStatus)
    dataCriacao = models.DateField(auto_now_add=True)
    dataEdicao = models.DateField(auto_now=True)

class Alerta (models.Model):
    class Meta:
        verbose_name = "Alerta"
        verbose_name_plural = "Alertas"

    def __str__(self):
        return self.descricao

    descricao = models.CharField(verbose_name="Descrição", max_length=200)
    licitacaoId = models.ForeignKey(Licitacao, verbose_name="Licitação", on_delete=models.CASCADE)
    destinatario = models.CharField(verbose_name="Destinatário", max_length=200)
    meioEnvioId = models.ForeignKey(MeioEnvio, verbose_name="Meio de envio", on_delete=models.CASCADE)
    dataCriacao = models.DateField(auto_now_add=True)
    dataEdicao = models.DateField(auto_now=True)

class Comentario (models.Model):
    class Meta:
        verbose_name = "Comentário"
        verbose_name_plural = "Comentários"

    def __str__(self):
        return self.descricao

    autor = models.CharField(verbose_name="Autor", max_length=100)
    descricao = models.CharField(verbose_name="Descrição", max_length=200)
    criticidade = models.CharField(verbose_name="Criticidade", max_length=50)
    licitacaoId = models.ForeignKey(Licitacao, verbose_name="Licitacão", on_delete=models.CASCADE)
    dataCriacao = models.DateField(auto_now_add=True)
    dataEdicao = models.DateField(auto_now=True)

class Documento (models.Model):
    class Meta:
        verbose_name = ("Documento")
        verbose_name_plural = ("Documentos")

    def __str__(self):
        return self.comentario

    comentario = models.CharField(verbose_name="Comentário", max_length=300)
    tipoId = models.ForeignKey(Tipo, verbose_name="Tipo de documento", on_delete=models.CASCADE)
    documento = models.FileField(verbose_name="Documento", upload_to="documentos")
    dataPublicacao = models.DateField(verbose_name="Data de publicação")
    licitacaoId = models.ForeignKey(Licitacao, verbose_name="Licitação", on_delete=models.CASCADE)
    dataCriacao = models.DateField(auto_now_add=True)
    dataEdicao = models.DateField(auto_now=True)

class Recolhimento (models.Model):
    class Meta:
        verbose_name = ("Recolhimento")
        verbose_name_plural = ("Recolhimentos")

    def __str__(self):
        return self.licitacao

    dataRecolhimento = models.DateField(verbose_name="Data de recolhimento")
    licitacaoId = models.ForeignKey(Licitacao, verbose_name="Licitação", on_delete=models.CASCADE)
    dataCriacao = models.DateField(auto_now_add=True)
    dataEdicao = models.DateField(auto_now=True)

class Publicacao (models.Model):
    class Meta:
        verbose_name = ("Publicação")
        verbose_name_plural = ("Publicações")

    def __str__(self):
        return self.licitacao

    dataPublicacao = models.DateField(verbose_name="Data de publicação")
    dataQuestionamento = models.DateField(verbose_name="Data para questionamento")
    dataImpugnacao = models.DateField(verbose_name="Data para impugnação")
    dataExecucao = models.DateField(verbose_name="Data para Execução")
    licitacaoId = models.ForeignKey(Licitacao, verbose_name="Licitação", on_delete=models.CASCADE)
    dataCriacao = models.DateField(auto_now_add=True)
    dataEdicao = models.DateField(auto_now=True)
