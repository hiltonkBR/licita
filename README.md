## Autor
Hilton Kevin de Carvalho

## Linguagem 
- Python com Framework Django

## Sobre
A ideia é gerir as licitações em que uma empresa esteja participando. A API possibilitará a integraçõa com outros sistemas da corporação.

## User Stories
- Como empresa eu desejo:
  - Cadastrar licitações
  - Atualizar licitações
  - Deleta licitações
  - Controlar as datas de questionamento, impugnação e certame gerando alertas para estas datas. 
  - Poder consultar as licitações correntes atraves de integração via API de outros sistemas.

## Endpoints
- Cria, lista, edita e deleta licitações.
  - [GET] lista licitações /licitacoes
  - [GET] lista licitação por ID /licitacoes/{id}
  - [POST] cria licitação /licitacoes
  - [DELETE] deleta licitação /licitacoes/{id}
  - [PUT] edita licitação /licitacoes/{id}/

- Cria, lista, edita e deleta alertas das licitações.
  - [GET] lista alertas /alertas
  - [GET] lista alerta por ID /alertas/{id}
  - [POST] cria alerta /alertas
  - [DELETE] deleta alerta /alertas/{id}
  - [PUT] edita alerta /alertas/{id}/

- Cria, lista, edita e deleta comentários das licitações.
  - [GET] lista comentários /comentarios
  - [GET] lista comentário por ID /comentarios/{id}
  - [POST] cria comentário /comentarios
  - [DELETE] deleta comentário /comentarios/{id}
  - [PUT] edita comentário /comentarios/{id}/

- Cria, lista, edita e deleta documentos das licitações.
  - [GET] lista documentos /documentos
  - [GET] lista documento por ID /documentos/{id}
  - [POST] cria documento /documentos
  - [DELETE] deleta documento /documentos/{id}
  - [PUT] edita documento /documentos/{id}/

- Cria, lista, edita e deleta datas de recolhimento das licitações.
  - [GET] lista recolhimentos /recolhimentos
  - [GET] lista recolhimento por ID /recolhimentos/{id}
  - [POST] cria recolhimento /recolhimentos
  - [DELETE] deleta recolhimento /recolhimentos/{id}
  - [PUT] edita recolhimento /recolhimentos/{id}/

- Cria, lista, edita e deleta datas de publicacão das licitações.
  - [GET] lista publicações /publicacoes
  - [GET] lista publicação por ID /publicacoes/{id}
  - [POST] cria publicação /publicacoes
  - [DELETE] deleta publicação /publicacoes/{id}
  - [PUT] edita publicação /publicacoes/{id}/

- Cria, lista, edita e deleta tipos de documentos que podem ser anexados as licitações.
  - [GET] lista tipos /tipos
  - [GET] lista tipo por ID /tipos/{id}
  - [POST] cria tipo /tipos
  - [DELETE] deleta tipo /tipos/{id}
  - [PUT] edita tipo /tipos/{id}/

- Cria, lista, edita e deleta tipos de documentos que podem ser anexados as licitações.
  - [GET] lista tipos /tipos
  - [GET] lista tipo por ID /tipos/{id}
  - [POST] cria tipo /tipos
  - [DELETE] deleta tipo /tipos/{id}
  - [PUT] edita tipo /tipos/{id}/

- Cria, lista, edita e deleta tecnologias das licitações.
  - [GET] lista tecnologias /tecnologias
  - [GET] lista tecnologia por ID /tecnologias/{id}
  - [POST] cria tecnologia /tecnologias
  - [DELETE] deleta tecnologia /tecnologias/{id}
  - [PUT] edita tecnologia /tecnologias/{id}/

- Cria, lista, edita e deleta Meio de Envio dos Alertas das licitações.
  - [GET] lista Meios de Envio /meios-de-envios
  - [GET] lista Meio de Envio por ID /meios-de-envios/{id}
  - [POST] cria Meio de Envio /meios-de-envios
  - [DELETE] deleta Meio de Envio /meios-de-envios/{id}
  - [PUT] edita Meio de Envio /meios-de-envios/{id}/

- Cria, lista, edita e deleta clientes.
  - [GET] lista clientes /clientes
  - [GET] lista cliente por ID /clientes/{id}
  - [POST] cria cliente /clientes
  - [DELETE] deleta cliente /clientes/{id}
  - [PUT] edita cliente /clientes/{id}/

- Cria, lista, edita e deleta contatos das licitações.
  - [GET] lista contatos /contato
  - [GET] lista contato por ID /contato/{id}
  - [POST] cria contato /contato
  - [DELETE] deleta contato /contato/{id}
  - [PUT] edita contato /contato/{id}/

- Cria, lista, edita e deleta links das licitações.
  - [GET] lista links /link
  - [GET] lista link por ID /link/{id}
  - [POST] cria link /link
  - [DELETE] deleta link /link/{id}
  - [PUT] edita link /link/{id}/