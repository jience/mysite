from django.urls import path
from . import views

from django.contrib.auth import views as auth_views


urlpatterns = [
    # path('login/', views.user_login, name='user_login'),
    path('login/', auth_views.login, name='user_login'),
    path('new-login/', auth_views.login, {"template_name": "account/login.html"}),
]

app_name = 'account'
