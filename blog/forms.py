from django import forms

from .models import Comment


# Formulario público para que visitantes puedan dejar comentarios.
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ["name", "email", "body"]
        widgets = {
            "name": forms.TextInput(attrs={"placeholder": "Tu nombre"}),
            "email": forms.EmailInput(attrs={"placeholder": "tu@email.com"}),
            "body": forms.Textarea(attrs={"placeholder": "Dejá una idea, una pregunta o una recomendación...", "rows": 5}),
        }
