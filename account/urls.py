from django.urls import path
from . import views

from django.contrib.auth import views as auth_views


urlpatterns = [
    # path('login/', views.user_login, name='user_login'),
    path('login/', auth_views.login, name='user_login'),
    path('new-login/', auth_views.login, {"template_name": "account/login.html"}),
    path('logout/', auth_views.logout, {"template_name": "account/logout.html"}, name='user_logout'),
    path('register/', views.register, name='user_register'),
]

app_name = 'account'
