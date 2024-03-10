# Self Created file.

from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request, 'index.html')
    # return HttpResponse('Home')


def removepunc(request):
    return HttpResponse('remove punctuations')


def captfirst(request):
    return HttpResponse('Capitalise first.')


def newlineremover(request):
    return HttpResponse('New Line Remover.')


def spaceremover(request):
    return HttpResponse('space remover')


def charcount(request):
    return HttpResponse('Character count')
