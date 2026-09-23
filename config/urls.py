from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

# El panel admin usa /admin/ y el resto de las rutas pertenece a la app blog.
urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("blog.urls")),
]

if settings.DEBUG:
    # Durante el desarrollo, Django sirve las imágenes subidas localmente.
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
