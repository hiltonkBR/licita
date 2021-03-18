from django.db import models
from contrib.models import Tecnologia, Tipo, MeioEnvio
from clientes.models import Cliente

class Licitacao (models.Model):
    class Meta:
        verbose_name = "Licitacão"
        verbose_name_plural = "Licitações"

    def __str__(self):
        return self.clienteID.nomeCliente

    choiceStatusLicitacao = (
        ("Publicada", "Publicada"),
        ("Recolhida", "Recolhida"),
        ("Republicada", "Republicada"),
        ("Encerrada", "Encerrada")
    )

    choicesStatusInterjato = (
            ("Em analise", "Em analise"),
            ("Faltando documentação", "Faltando documentação"),
            ("Apta", "Apta"),
            ("Conquistada", "Conquistada"),
            ("Inapta", "Inapta")
    )
    
    clienteID = models.ForeignKey(Cliente, verbose_name="cliente", on_delete=models.CASCADE)
    pregao = models.CharField(verbose_name="Número do pregão",  max_length=50)
    uasg = models.IntegerField(verbose_name="Número do UASG", null=True)
    objeto = models.TextField(verbose_name="Objeto da Licitação")
    tecnologiaId = models.ManyToManyField(Tecnologia, verbose_name="Tecnologias")
    objeto = models.TextField(verbose_name="Objeto da licitação", null=True)
    valorEstimado = models.FloatField(verbose_name="Valor estimado", null=True)
    observacoes = models.TextField(verbose_name="Observações", null=True)
    statusLicitacao = models.CharField(verbose_name="Situação da Licitação", max_length=11, choices=choiceStatusLicitacao)
    statusInterjato = models.CharField(verbose_name="Status da Licitação", max_length=50, choices=choicesStatusInterjato, null=True)
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

    choiseCriticidade = (
            (1, "Urgente"),
            (2, "Alta"),
            (3, "Media"),
            (4, "Informação")
    )

    autor = models.CharField(verbose_name="Autor", max_length=100)
    comentario = models.TextField(verbose_name="Comentario", max_length=200)
    documento = models.FileField(verbose_name="Documento", upload_to="documentos", null=True)
    criticidade = models.CharField(verbose_name="Criticidade", max_length=50, choices=choiseCriticidade)
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
