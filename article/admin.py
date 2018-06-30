from django.contrib import admin
from article.models import ArticleColumn


# Register your models here.
class ArticleColumnAdmin(admin.ModelAdmin):
    list_display = ('column', 'created', 'user')
    list_filter = ("column",)


admin.site.register(ArticleColumn, ArticleColumnAdmin)
