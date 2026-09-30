from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from django.views.generic import TemplateView

urlpatterns = [
    path("admin/", admin.site.urls),
    path("blog/", include("blog.urls")),
    path("", TemplateView.as_view(template_name="index.html"), name="portfolio"),
]

if settings.DEBUG:
    # Durante el desarrollo, Django sirve las imágenes subidas localmente.
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
