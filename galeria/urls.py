from django.conf.urls.defaults import url, patterns
from galeria.views import CadastrarImagem, AlterarImagem, ListarImagem,\
        RemoverImagem

urlpatterns = patterns('galeria.views',
        url(r'^show/$', 'show'),
        url(r'^cadastrar/$', CadastrarImagem.as_view(), name='cadastrar-imagem'),
        url(r'^alterar/(?P<pk>\d+)$', AlterarImagem.as_view(), name='alterar-imagem'),
        url(r'^listar/$', ListarImagem.as_view(), name='listar-imagem'),
        url(r'^remover/(?P<pk>\d+)$', RemoverImagem.as_view(), name='remover-imagem'),
)
