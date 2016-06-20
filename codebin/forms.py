from django import forms
from snowpenguin.django.recaptcha2.fields import ReCaptchaField
from snowpenguin.django.recaptcha2.widgets import ReCaptchaWidget
from .models import Snippet


class SnippetForm(forms.ModelForm):
    captcha = ReCaptchaField(widget=ReCaptchaWidget())

    class Meta:
        model = Snippet
        exclude = ('created_date', 'author')
