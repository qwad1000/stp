from django import forms

from .models import Snippet


class SnippetForm(forms.ModelForm):
    class Meta:
        model = Snippet
        exclude = ('created_date', )
