from django.views.generic import TemplateView


class AboutView(TemplateView):
    template_name = "janeiro/about.html"


class CareersView(TemplateView):
    template_name = "janeiro/careers.html"


class ContactsView(TemplateView):
    template_name = "janeiro/contacts.html"


class NewsView(TemplateView):
    template_name = "janeiro/news.html"


class NewsDetailView(TemplateView):
    template_name = "janeiro/news_detail.html"


class ServicesView(TemplateView):
    template_name = "janeiro/services.html"


class HomeView(TemplateView):
    template_name = "janeiro/index.html"
