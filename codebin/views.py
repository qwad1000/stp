from django.shortcuts import render, get_object_or_404, redirect, Http404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.utils import timezone

from .models import Snippet
from .forms import SnippetForm
from .search import *
# Create your views here.

max_pages = 10
max_per_page = 10
max_snippets = max_pages * max_per_page


def _list_snippets(user, my=None):
    if user.is_authenticated():
        if my:  # get only my snippets (both public and private)
            return Snippet.objects.filter(Q(author=user))
        else:  # get public and my snippets
            return Snippet.objects.filter(Q(private=Snippet.PUBLIC) | (Q(author=user) & ~Q(private=Snippet.PUBLIC)))
    else:
        return Snippet.objects.filter(Q(private=Snippet.PUBLIC))


def snippet_list(request, my):
    snippets = _list_snippets(request.user, my)

    paged_snippets = _paginate(request, snippets.order_by('-created_date')[:max_snippets])
    return render(request, 'codebin/snippet_list.html', {'snippets': paged_snippets})


def snippet_view(request, base58):
    snippet = get_object_or_404(Snippet, base58=base58)
    if snippet.private == Snippet.PRIVATE and request.user != snippet.author:
        raise Http404('No snippet.')
    return render(request, 'codebin/snippet_view.html', {'snippet': snippet})


def snippet_new(request):
    errors = []
    if request.method == 'POST':
        form = SnippetForm(request.POST)
        if form.is_valid():
            snippet = form.save(commit=False)
            if request.user.is_authenticated():
                snippet.author = request.user

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
        found = _list_snippets(request.user, my=None)\
                    .filter(query)\
                    .order_by('-created_date')[:max_snippets]
    else:
        return redirect('snippet_list')

    return render(request, 'codebin/snippet_list.html',
                  {'snippets': _paginate(request, found),
                   'query_string': query_string})


def _paginate(request, snippets):
    paginator = Paginator(snippets, max_per_page)

    page = request.GET.get('page')
    try:
        snippets = paginator.page(page)
    except (PageNotAnInteger, EmptyPage):
        snippets = paginator.page(1)

    return snippets
