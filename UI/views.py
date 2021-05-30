from django.shortcuts import render
from django.http import HttpResponse
from Summarisation.utils.text_rank import generate_summary
from Summarisation.summarizer.model_processors import Summarizer
from Classification.utils.SVC_model_TC import predict as svc_predict
from Classification.utils.LSTM_model.LSTM_model_TC import predict as lstm_predict
from TopicModelling.utils.lda_model import get_topics
from TopicModelling.utils.lsa import modelTopics
from TopicModelling.views import lda_textProcessing

# bert_model = Summarizer()

def index(request):
    return render(request, 'UI/index.html', {})

def summarisation(data):
    method1_data = generate_summary(data)
    # method2_data = bert_model(data)
    value = {
            'method1_name': 'Text Rank',
            'method1_data': method1_data,
            'method2_name': 'BERT',
            'method2_data': "Just a place holder for now"
    }
    return value

def classificaion(data):
    method1_data = svc_predict(data)[0]
    method2_data = lstm_predict(data)
    value = {
            'method1_name': 'SVC',
            'method1_data': method1_data,
            'method2_name': 'LSTM',
            'method2_data': method2_data
    } 
    return value

def titling():
    return HttpResponse('Chyottomate! Still in devlopment')

def topic_modelling(data, topic_number, word_number):
    method1_data = lda_textProcessing(data)
    method2_data = modelTopics(data)
    value = {
            'method1_name': 'LDA',
            'method1_data': method1_data,
            'method2_name': 'LSA',
            'method2_data': method2_data
    } 
    return value

def handle_common_request(request):
    data = request.POST['data']
    if request.POST['button'] == 'summarise':
        print("summarisation")
        context = summarisation(data)

    elif request.POST['button'] == 'classify':
    	print(request.POST['data'])
    	context = classificaion([request.POST['data']])
        
    elif request.POST['button'] == 'titling':
        topic_number = max(0, int(request.POST['topic_number']))
        word_number = max(0, int(request.POST['word_number']))
        context = titling(topic_number, word_number)

    elif request.POST['button'] == 'topic modelling':
        topic_number = max(0, int(request.POST['topic_number']))
        word_number = max(0, int(request.POST['word_number']))
        context = topic_modelling(data, topic_number, word_number)
    
    return render(request, 'UI/results.html', context)
