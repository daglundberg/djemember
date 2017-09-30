from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.auth import views as auth_views
from minnesboken import views

urlpatterns = [
    url(r'^login/$', auth_views.login, {'template_name': 'templates/login.html'}, name='login'),
    url(r'^logout/$', auth_views.logout, {'template_name': 'templates/logout.html'}, name='logout'),
    url(r'^minnen/', include('minnesboken.urls')),
    url(r'^admin/', admin.site.urls),
    url(r'^texter/$', views.writings, name='list_of_writings'),
    url(r'^texter/(?P<writing_id>[0-9]+)/$', views.writing_detail, name='writing_detail'),
    url(r'^$', views.landingpage, name='landingpage'),
    url(r'^accounts/', include('allauth.urls')),
]
