from django.contrib import messages
from django.http import HttpResponseBadRequest
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse
from django.utils.http import url_has_allowed_host_and_scheme
from django.views.decorators.http import require_POST

from .forms import CommentForm
from .models import Post


@require_POST
def set_theme(request):
    theme = request.POST.get("theme")
    if theme not in {"dark", "light"}:
        return HttpResponseBadRequest("Tema no válido.")

    request.session["theme"] = theme
    next_url = request.POST.get("next", "")
    if url_has_allowed_host_and_scheme(
        next_url,
        allowed_hosts={request.get_host()},
        require_https=request.is_secure(),
    ):
        return redirect(next_url)
    return redirect(reverse("portfolio"))


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
