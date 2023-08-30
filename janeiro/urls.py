from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from janeiro import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('hospital.urls'))
]
static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
