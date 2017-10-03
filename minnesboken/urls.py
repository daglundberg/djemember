from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^dtempdtemp/$', views.direct_upload_complete, name='direct_upload_complete'),
    url(r'^dela-ett-minne/$', views.share_a_memory, name='share_a_memory'),
    url(r'^$', views.memories, name='memories'),
    url(r'^(?P<memory_id>[0-9]+)/$', views.memory_detail, name='memory_detail'),
    url(r'^bilder/$', views.pictures, name='pictures'),
    url(r'^bilder/(?P<picture_id>[0-9]+)/$', views.picture_detail, name='picture_detail'),
    url(r'^bilder/$', views.pictures, name='create_account'),
    url(r'^minneslinje/$', views.timeline, name='timeline')
]
