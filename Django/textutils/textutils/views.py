# Self created file.


from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    # Render the index.html template
    return render(request, 'index.html')


def analyze(request):
    # Get the text input from the request
    text = request.GET.get('text','default')
    
    # Check if the removepunc parameter is set to 'on'
    removepunc = request.GET.get('removepunc','off')
    
    if removepunc == 'on':
        # Initialize an empty string to store the analyzed text
        analyzed = ""
        
        # Define a string of punctuation characters
        punctuations = '''!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~'''

        # Iterate over each character in the input text
        for char in text:
            # Check if the character is not a punctuation character
            if char not in punctuations:
                # Append the character to the analyzed string
                analyzed = analyzed + char

        # Create a dictionary of parameters to pass to the analyze.html template
        params = {'purpose':'Remove Punctuations', 'analyzed_text': analyzed}
        
        # Render the analyze.html template with the parameters
        return render(request, 'analyze.html', params)
    
    else:
        # If the removepunc parameter is not set to 'on', return an error message
        return HttpResponse('Error. Please check the box.')

