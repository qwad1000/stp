from django.shortcuts import render
from django.utils import timezone
from .models import Snippet
# Create your views here.


def snippet_list(request):
    snippets = Snippet.objects.filter(created_date__lte=timezone.now()).order_by('created_date')[:10]
    return render(request, 'codebin/snippet_list.html', {'snippets': snippets})
