from django.urls import path
from . import views


urlpatterns = [
    path('', views.landingpage, name='landingpage'),
    path('signup/', views.signup, name="signup"),
    path('users/<username>/', views.user_detail, name='user_detail'),
]
