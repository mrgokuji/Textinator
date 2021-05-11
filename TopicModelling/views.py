from rest_framework.decorators import api_view
from django.http import HttpResponse
from .utils.lda_model import get_topics
from .utils.lsa import modelTopics
import json

@api_view(['POST',])
def get_lda_topics(request):
    data = request.data
    t = get_topics(data['para'],num_topics=3)
    print(t)
    t1 = [i[1] for i in t]
    topics = []
    for i in t1:
    	q = i.split('*')[1:]
    	e = [j.split(' + ') for j in q]
    	st = ""
    	for j in e:
    		st = st + j[0][1:-1] + ' '
    	
    	topics.append(st)
    	topics.append(',')
    print(topics)
    return HttpResponse(topics[:-1])
    
@api_view(['POST',])
def get_lsa_topics(request):
    data = request.data
    topics = modelTopics(data['para'])
    jsonString = json.dumps(topics)

    return HttpResponse(jsonString)
