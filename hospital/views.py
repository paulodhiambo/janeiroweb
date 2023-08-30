from django.shortcuts import get_object_or_404
from django.views.generic import TemplateView, ListView
from django.views.generic.detail import SingleObjectMixin, DetailView

from hospital.models import Article


class AboutView(TemplateView):
    template_name = "janeiro/about.html"


class CareersView(TemplateView):
    template_name = "janeiro/careers.html"


class ContactsView(TemplateView):
    template_name = "janeiro/contacts.html"


class NewsView(ListView):
    model = Article
    context_object_name = 'articles'
    paginate_by = 2
    queryset = Article.objects.filter(is_draft=False)
    template_name = "janeiro/news.html"


class NewsDetailView(DetailView):
    model = Article
    template_name = "janeiro/news_detail.html"
    context_object_name = 'article'
    slug_field = 'slug'
    slug_url_kwarg = 'slug'

    def get_object(self, queryset=None):
        slug = self.kwargs.get(self.slug_url_kwarg)
        queryset = queryset or self.get_queryset()
        return get_object_or_404(queryset, **{self.slug_field: slug})


class ServicesView(TemplateView):
    template_name = "janeiro/services.html"


class HomeView(TemplateView):
    template_name = "janeiro/index.html"
