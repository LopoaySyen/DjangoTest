from django.http import HttpResponse
from django.shortcuts import render


def hello(request):
    return HttpResponse('Hello World!')

def test(request):
    context = {}
    context = {'hello':'A test charsequence!!!','name':'Cooc'}
    return render(request, 'test.html', context)