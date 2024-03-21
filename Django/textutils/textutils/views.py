# Self created file.
from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    # return HttpResponse("Home")
    return render(request, 'index.html')
def analyze(request):
    return HttpResponse("Analyze Text.")

'''
# def removepunc(request):
#     return HttpResponse("Remove Punctuations")
# def capitalizefirst(request):
#     return HttpResponse("Capitalize First")
# def newlineremover(request):
#     return HttpResponse("New line Remover")
# def spaceremover(request):
#     return HttpResponse("Sapce Remover")
# def charcounter(request):
#     return HttpResponse("Char Counter") '''