# Self created file.
from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    # return HttpResponse("Home")
    return render(request, 'index.html')
def analyze(request):
    text = request.GET.get('text','default')

    analyzed = ""
    punctuations = '''!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~'''

    for char in text:
        if char not in punctuations:
            analyzed = analyzed + char

    params = {'purpose':'Remove Punctuations', 'analyzed_text': analyzed}
    return render(request, 'analyze.html', params)
