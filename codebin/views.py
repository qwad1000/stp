from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Snippet
# Create your views here.


def snippet_list(request):
    snippets = Snippet.objects.filter(created_date__lte=timezone.now()).order_by('created_date')[:10]
    return render(request, 'codebin/snippet_list.html', {'snippets': snippets})


def snippet_view(request, base58):
    snippet = get_object_or_404(Snippet, base58=base58)
    content = snippet.get_content()
    return render(request, 'codebin/snippet_view.html', {'snippet': snippet, 'content': content})
