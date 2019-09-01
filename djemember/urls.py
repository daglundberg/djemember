from django.conf.urls import include
from django.contrib import admin
from memories import views
from django.urls import path

urlpatterns = [
    path('memories/', include('memories.urls')),
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('', include('core.urls')),
]
