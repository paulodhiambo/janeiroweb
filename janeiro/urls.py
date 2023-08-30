from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from janeiro import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('hospital.urls')),
    path('ckeditor/', include('ckeditor_uploader.urls')),
]
static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

admin.site.site_header = "Janeiro Hospital"
admin.site.site_title = "Janeiro Hospital"
