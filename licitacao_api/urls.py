"""licitacao_api URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from rest_framework import routers
from licitacoes.views import *
from contrib.views import *
from clientes import views
from rest_framework_swagger.views import get_swagger_view
from django.conf.urls import url

schema_view = get_swagger_view(title='Licita')

router = routers.DefaultRouter()
router.register(r'alertas', AlertaViewSet)
router.register(r'comentarios', ComentarioViewSet)
router.register(r'licitacoes', LicitacaoViewSet)
router.register(r'documentos', DocumentoViewSet)
router.register(r'recolhimentos', RecolhimentoViewSet)
router.register(r'publicacoes', PublicacaoViewSet)
router.register(r'tipos', TipoViewSet)
router.register(r'tecnologias', TecnologiaViewSet)
router.register(r'meios-de-envios', MeioEnvioViewSet)
router.register(r'clientes', views.ClienteView, 'clientes')
router.register(r'contato', ContatoViewSet)
router.register(r'link', LinkViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('admin/', admin.site.urls),
    url(r'^docs/', schema_view)
]
