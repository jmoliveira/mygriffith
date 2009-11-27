from django.conf.urls.defaults import *
from django.conf import settings
from views import *

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    (r'^media/(.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),


    (r'^filmes$', filmes),

    (r'^admin/', include(admin.site.urls)),

    (r'^comments/', include('django.contrib.comments.urls')),
)
