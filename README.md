## Autor
Hilton Kevin de Carvalho

## Linguagem 
- Python com Django

## Sobre
A ideia é gerir as licitações em que uma empresa esteja participando. A API possibilita a integraçõa com outros sistemas da corporação.

## User Stories
- Como empresa eu desejo:
  - Cadastrar licitações
  - Atualizar licitações
  - Deleta licitações
  - Controlar as datas de questionamento, impugnação e certame gerando alertas para estas datas. 
  - Poder consultar as licitações correntes atraves de integração via API de outros sistemas.

## Endpoints
- Cria, lista licitações.
  - [GET] lista licitações /api/licita
  - [GET] lista licitação por ID /api/licita/{id}
  - [POST] cria licitações /api/licita
  - [DELET] deleta licitação /api/licita/{id}
  - [DELETE] deleta licitação /api/licita/{id}
  - [PUT] edita licitação /api/licita/{id}/

## Foi feita adição dos testes e CI
