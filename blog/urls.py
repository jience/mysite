from django.urls import path
from . import views


urlpatterns = [
    path(r'', views.blog_title, name="blog_title"),
    path(r'<article_id>', views.blog_article, name="blog_article")
]

app_name = 'blog'  # django 2.0 的include中需要定义app_name
