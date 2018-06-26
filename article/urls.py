from django.conf.urls import url
from article import views


urlpatterns = [
    url(r'^article-column/$', views.article_column, name="article_column"),
]
