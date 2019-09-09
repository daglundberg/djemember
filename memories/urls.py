from django.urls import path
from . import views, views_upload, views_posting, views_test

urlpatterns = [
    # View memories
    path('', views.memories, name='memories'),
    path('<int:memory_id>/', views.memory_detail, name='memory_detail'),

    # Post memories
    path('post/text/', views_posting.post_memory, name='post_memory'),
    path('post/comment/<int:timeline_item_id>', views_posting.post_comment, name='post_comment'),

    # View pictures
    # path('pictures/', views.pictures, name='pictures'),
    # path('pictures/<int:picture_id>/', views.picture_detail, name='picture_detail'),

    # Timeline
    path('timeline/', views.timeline, name='timeline'),
    path('upload/', views_upload.images_upload, name='upload'),
    path('upload/post', views_upload.testy, name='create-image-post'),
    path('megaform', views_test.megaform, name='megaform')
] 
