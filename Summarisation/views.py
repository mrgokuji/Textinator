from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .utils.text_rank import generate_summary
from .summarizer.model_processors import Summarizer

# model = Summarizer()

@api_view(['POST',])
def get_summary_text_rank(request):
    """this is mainly for the text ranking summarisation algorithm
        {
            "para":"some text with atleast 2 full stops(.)"
        }
    Args:
        request (HttpRequest): post request with data in above format

    Returns:
        HttpResponse: Text summarised Data
    """    
    # print(request.data)
    data = request.data
    summary = generate_summary(data['para'])
    print(summary)
    return HttpResponse(summary)
    # return Response(status=200,data=request)

"""@api_view(['POST',])
def get_summary_bert(request):
    data = request.data
    summary = model(data['para'])
    return HttpResponse(summary)
"""

@api_view(['GET'])
def get_summary_details(request):
    data = '''<h1>Welcome to website of Summarizer!!!</h1>
              following are the urls for accessing different summarizers.<br>
              'summarise/text_rank' <---- for text rank algorithm.<br>
              'summarise/bert'   <----- for bert extractive summarizer.<br>
    '''
    return HttpResponse(data)

