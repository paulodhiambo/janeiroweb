from django.urls import path

from hospital.views import AboutView, CareersView, ContactsView, NewsView, NewsDetailView, ServicesView, HomeView

urlpatterns = [
    path("about/", AboutView.as_view(), name="about"),
    path("careers/", CareersView.as_view(), name="careers"),
    path("contacts/", ContactsView.as_view(), name="contacts"),
    path("news/", NewsView.as_view(), name="news"),
    path("detail/", NewsDetailView.as_view(), name="detail"),
    path("services/", ServicesView.as_view(), name="services"),
    path("", HomeView.as_view(), name="index"),
]
