# Self Created file.

from django.http import HttpResponse


def index(request):
    return HttpResponse('Hello')
