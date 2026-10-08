from django.urls import path

from . import views

# Rutas públicas del blog: listado general y detalle de una entrada.
urlpatterns = [
    path("", views.post_list, name="post_list"),
    path("entrada/<slug:slug>/", views.post_detail, name="post_detail"),
    path("tema/", views.set_theme, name="set_theme"),
]
