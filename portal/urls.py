from django.conf.urls import patterns, include, url
from django.conf import settings

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'portal.views.home', name='home'),
    # url(r'^portal/', include('portal.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'galeria.views.show'),
    url(r'^galeria/', include('galeria.urls')),

    # ----------- Carregar Arquivos Estaticos ----------- #
    (r'^media/(.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),

)
