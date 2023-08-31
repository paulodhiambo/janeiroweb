from django.contrib import admin
from django.contrib.auth.models import Group

from hospital.forms import ArticleAdminForm, CareerAdminForm
from hospital.models import Article, Career


# Register your models here.
@admin.register(Article)
class ArticlesAdmin(admin.ModelAdmin):
    form = ArticleAdminForm
    model = Article
    list_display = ["title_summary", "created_at", "published_at", "is_draft", ]
    list_filter = ["created_at", "is_draft", ]


@admin.register(Career)
class CareersAdmin(admin.ModelAdmin):
    form = CareerAdminForm
    model = Career
    list_display = ["title", "published_at", "is_open", ]
    list_filter = ["published_at", "is_open", ]


admin.site.unregister(Group)
