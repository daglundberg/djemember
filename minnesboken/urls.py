from django.conf.urls import url

from . import views

urlpatterns = [
    # Create memories
    url(r'^post-timeline-memory/$', views.new_timeline_post, name='new_timeline_post'),
    url(r'^post-memory/$', views.new_post, name='new_post'),

    # View memories
    url(r'^$', views.memories, name='memories'),
    url(r'^(?P<memory_id>[0-9]+)/$', views.memory_detail, name='memory_detail'),

    # View pictures
    url(r'^bilder/$', views.pictures, name='pictures'),
    url(r'^bilder/(?P<picture_id>[0-9]+)/$', views.picture_detail, name='picture_detail'),

    # Timeline
    url(r'^minneslinje/$', views.timeline, name='timeline')
]
