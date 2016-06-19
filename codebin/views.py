from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone

from .models import Snippet
from .forms import SnippetForm
from .search import *
# Create your views here.


def snippet_list(request):
    snippets = Snippet.objects.filter(created_date__lte=timezone.now()).order_by('created_date')[:10]
    return render(request, 'codebin/snippet_list.html', {'snippets': snippets})


def snippet_view(request, base58):
    snippet = get_object_or_404(Snippet, base58=base58)
    return render(request, 'codebin/snippet_view.html', {'snippet': snippet})


def snippet_new(request):
    errors = []
    if request.method == 'POST':
        form = SnippetForm(request.POST)
        if form.is_valid():
            snippet = form.save(commit=False)
            snippet.save()
            return redirect('snippet_view', base58=snippet.base58)
    else:
        form = SnippetForm()
    return render(request, 'codebin/snippet_edit.html', {'errors': errors, 'form': form})


def search(request):
    query_string = ''
    found = None
    if ('q' in request.GET) and request.GET['q'].strip():
        query_string = request.GET['q']

        query = get_query(query_string, ['title'])
        found = Snippet.objects.filter(query).order_by('created_date')[:10]
    else:
        return redirect('snippet_list')

    return render(request, 'codebin/snippet_list.html', {'snippets': found,
                                                         'query_string': query_string})

