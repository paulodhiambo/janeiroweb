from django.contrib import admin
from django.contrib.auth.models import Group

from hospital.forms import ArticleAdminForm
from hospital.models import Article


# Register your models here.
@admin.register(Article)
class ArticlesAdmin(admin.ModelAdmin):
    form = ArticleAdminForm
    model = Article
    list_display = ["title_summary", "created_at", "published_at", "is_draft", ]
    list_filter = ["created_at", "is_draft", ]


admin.site.unregister(Group)
