from django.contrib import admin

from .models import Comment, Post


# Configuración del panel para crear y editar entradas.67
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ("title", "category", "published_at")
    list_filter = ("category", "published_at")
    search_fields = ("title", "excerpt", "content")
    prepopulated_fields = {"slug": ("title",)}


# Configuración del panel para consultar y eliminar comentarios.
@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ("name", "post", "created_at")
    list_filter = ("created_at",)
    search_fields = ("name", "email", "body", "post__title")
    readonly_fields = ("created_at",)
