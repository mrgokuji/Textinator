from django.urls import path
from .views import get_text_classification_svc ,get_text_classification_lstm
app_name = 'Classification'

urlpatterns = [
    path('SVC/', get_text_classification_svc),
    path('LSTM/', get_text_classification_lstm),
]
