# Self created file.


from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    # Render the index.html template
    return render(request, 'index.html')


def analyze(request):
    # Get the text input from the request
    input_text = request.POST.get('text','default')
    # Check if the removepunc parameter is set to 'on'
    removepunc = request.GET.get('removepunc','off')
    # Check if the uppercase parameter is set to 'on'
    uppercase = request.GET.get('uppercase','off')
    # Check if the newlineremover parameter is set to 'on'
    newlineremover = request.GET.get('newlineremover','off')
    # Check if the spaceremover parameter is set to 'on'
    extraspaceremover = request.GET.get('extraspaceremover','off')
    # Check if the charcounter parameter is set to 'on'
    charcounter = request.GET.get('charcounter','off')
    
    if removepunc == 'on':

        analyzed = ""
        punctuations = '''!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~'''

        for char in input_text:
            if char not in punctuations:
                analyzed = analyzed + char

        # Create a dictionary of parameters to pass to the analyze.html template
        params = {'purpose':'Removed Punctuations', 'analyzed_text': analyzed}
        
        # Render the analyze.html template with the parameters
        return render(request, 'analyze.html', params)
    
    elif(uppercase == 'on'):
        analyzed = ''
        for char in input_text:
            analyzed = analyzed + char.upper()

        params = {'purpose':'Changed to UpperCase', 'analyzed_text': analyzed}
        return render(request, 'analyze.html', params)
    
    elif(newlineremover=='on'):
        analyzed = ''
        for char in input_text:
            if char !='\n':
                analyzed = analyzed + char

        params = {'purpose':'Removed new lines.', 'analyzed_text': analyzed}
        return render(request, 'analyze.html', params)
    
    elif(extraspaceremover=='on'):
        analyzed = ' '.join(input_text.split())
        
        params = {'purpose':'Removed spaces.', 'analyzed_text': analyzed}
        return render(request, 'analyze.html', params)
    
    elif(charcounter=='on'):

        analyzed = (f'{input_text} has {len(input_text)} characters.')

        params = {'purpose':'Counted Characters.', 'analyzed_text': analyzed}
        return render(request, 'analyze.html', params)

    else:
        return HttpResponse('Error. Please tick the checkbox.')

