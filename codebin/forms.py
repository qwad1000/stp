from django import forms

from .models import Snippet


class SnippetForm(forms.ModelForm):
    form_content = forms.CharField(label="Snippet", widget=forms.Textarea())

    class Meta:
        model = Snippet
        exclude = ('created_date', )
