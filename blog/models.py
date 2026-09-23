from django.db import models
from django.urls import reverse
from django.utils.text import slugify


# Representa cada entrada publicada en el blog.
class Post(models.Model):
    title = models.CharField("título", max_length=180)
    slug = models.SlugField("slug", unique=True, blank=True)
    excerpt = models.TextField("bajada", max_length=300)
    content = models.TextField("contenido")
    cover = models.ImageField("imagen de portada", upload_to="posts/", blank=True, null=True)
    category = models.CharField("categoría", max_length=80, default="Ideas")
    published_at = models.DateTimeField("fecha de publicación", auto_now_add=True)
    updated_at = models.DateTimeField("última edición", auto_now=True)

    class Meta:
        ordering = ["-published_at"]
        verbose_name = "entrada"
        verbose_name_plural = "entradas"

    def save(self, *args, **kwargs):
        # Genera una URL amigable automáticamente a partir del título.
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        # Permite que Django obtenga la URL pública de la entrada.
        return reverse("post_detail", kwargs={"slug": self.slug})

    def __str__(self):
        return self.title


# Comentario enviado por una persona en una entrada determinada.
class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comments", verbose_name="entrada")
    name = models.CharField("nombre", max_length=80)
    email = models.EmailField("email")
    body = models.TextField("comentario", max_length=600)
    created_at = models.DateTimeField("fecha", auto_now_add=True)

    class Meta:
        ordering = ["created_at"]
        verbose_name = "comentario"
        verbose_name_plural = "comentarios"

    def __str__(self):
        return f"{self.name} en {self.post.title}"
