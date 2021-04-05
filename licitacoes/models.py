from django.db import models
from contrib.models import Tecnologia, Tipo, MeioEnvio
from clientes.models import Cliente

class Licitacao (models.Model):
    class Meta:
        verbose_name = "Licitacão"
        verbose_name_plural = "Licitações"

    def __str__(self):
        return self.clienteGerenciadorID.nomeCliente

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

    choicesTipoPregao = (
            ("Presencial", "Presencial"),
            ("Eletrônico", "Eletrônico")
    )

    choicesModalidade = (
            ("Carta convite", "Carta convite"),
            ("Emergencial", "Emergencial"),
            ("Chamada pública", "Chamada pública"),
            ("Shopping", "Shopping"),
            ("Concorrência", "Concorrência"),
            ("Tomada de preços", "Tomada de preços"),
            ("Pregão", "Pregão")
    )
    
    clienteGerenciadorID = models.ForeignKey(Cliente, verbose_name="Cliente Gerenciador", related_name="clienteGerenciadorID", on_delete=models.CASCADE)
    clienteBeneficiadoID = models.ForeignKey(Cliente, verbose_name="Cliente Beneficiado", related_name="clienteBeneficiadoID", on_delete=models.CASCADE)
    modalidadeLicitacao = models.CharField(verbose_name="Modalidade da Licitação", max_length=25, choices=choicesModalidade)
    tipoPregao = models.CharField(verbose_name="Tipo de Pregão", max_length=25, choices=choicesTipoPregao, null=True)
    numLicitacao = models.CharField(verbose_name="Código da pregão",  max_length=50, null=True)
    registroPreco = models.BooleanField(verbose_name="Registro de preço?")
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

class Contato (models.Model):
    class Meta:
        verbose_name = ("Contato")
        verbose_name_plural = ("Documentos")
    
    def __str__(self):
        return self.nome
    
    nome = models.CharField(verbose_name="Nome do contato", max_length=100)
    funcao = models.CharField(verbose_name="Função do contato", max_length=100)
    telefone = models.CharField(verbose_name="Telefone do contato", max_length=50, null=True)
    email = models.CharField(verbose_name="E-mail do contato", max_length=100, null=True)
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

class Link (models.Model):
    class Meta:
        verbose_name = ("Link")
        verbose_name_plural = ("Links")

    def __str__(self):
        return self.tipoLink

    choiseTipoLink = (
            ("Questionamentos", "Questionamentos"),
            ("Impugnação", "Impugnação"),
            ("Anuncios", "Anuncios"),
            ("Documentos", "Documentos")
    )

    tipoLink = models.CharField(verbose_name="Tipo do Link", max_length=50, choices=choiseTipoLink)
    link = models.TextField(verbose_name="Link")
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
