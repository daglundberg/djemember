from django.urls import path

from . import views

urlpatterns = [
    # View memories
    path('', views.memories, name='memories'),
    path('<int:memory_id>/', views.memory_detail, name='memory_detail'),

    # Post memories
    # path('create-post/', views.create_post, name='create_post'),

    # View pictures
    # path('pictures/', views.pictures, name='pictures'),
    # path('pictures/<int:picture_id>/', views.picture_detail, name='picture_detail'),

    # Timeline
    # path('timeline/', views.timeline, name='timeline')
]
