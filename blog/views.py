from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect, render

from .forms import CommentForm
from .models import Post


def post_list(request):
    # Las entradas ya vienen ordenadas por fecha desde el modelo.
    posts = Post.objects.all()
    featured = posts.first()
    return render(request, "blog/post_list.html", {"posts": posts, "featured": featured})


def post_detail(request, slug):
    # Busca la entrada por su slug y devuelve 404 si no existe.
    post = get_object_or_404(Post, slug=slug)
    comments = post.comments.all()
    form = CommentForm(request.POST or None)

    # Procesa el formulario y redirige para evitar reenvíos al actualizar.
    if request.method == "POST" and form.is_valid():
        comment = form.save(commit=False)
        comment.post = post
        comment.save()
        messages.success(request, "Tu comentario ya está publicado. Gracias por compartir.")
        return redirect(post.get_absolute_url())

    return render(request, "blog/post_detail.html", {"post": post, "comments": comments, "form": form})
