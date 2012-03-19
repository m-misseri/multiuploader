from django.conf.urls.defaults import *

urlpatterns = patterns('',
    url(r'^multi_delete/(\d+)/$', 'multiuploader.views.multiuploader_delete', name='multi_delete'),
    url(r'^multi/$', 'multiuploader.views.multiuploader', name='multi'),
    url(r'^multi_image/(\d+)/$', 'multiuploader.views.multi_show_uploaded'),
)