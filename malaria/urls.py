from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from malaria import settings

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^dados/mapa/', 'malaria.dados.views.mapa'),
    url(r'^dados/informativo/', 'malaria.dados.views.informativo'),
    url(r'^dados/estatisticas/', 'malaria.dados.views.estatisticas'),
    url(r'^dados/sobre/', 'malaria.dados.views.sobre'),
    url(r'^dados/', 'malaria.dados.views.index'),
    url(r'^admin/', include(admin.site.urls)),
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += staticfiles_urlpatterns()