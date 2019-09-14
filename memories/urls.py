from django.urls import path
from . import views, views_create
from django.views.generic import TemplateView

urlpatterns = [
    # View memories
    path('', views.post_list, name='post_list'),
    path('<int:text_id>/', views.post_detail, name='post_detail'),

    # Upload
    path('upload/', views.images_upload, name='upload'),

    # Create posts
    path('create/', TemplateView.as_view(template_name='memories/choose_post_type.html'), name='create'),
    path('create/comment/<int:post_id>', views_create.comment_create, name='comment_create'),
    path('create/post/', views_create.post_create, name='post_create'),
    path('create/album/', views_create.album_create, name='album_create'),

    # Timeline
    path('timeline/', views.timeline, name='timeline'),
]
