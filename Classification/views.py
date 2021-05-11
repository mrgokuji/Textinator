from sklearn.feature_extraction.text import CountVectorizer
from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .utils.SVC_model_TC import predict as svc_predict
from .utils.LSTM_model.LSTM_model_TC import predict as lstm_predict

@api_view(['POST'])
def get_text_classification_svc(request):
    data = request.data
    summary = svc_predict([data["para"]])
    return HttpResponse(summary)


@api_view(['POST'])
def get_text_classification_lstm(request):
    data = request.data
    summary = lstm_predict([data["para"]])
    return HttpResponse(summary)
