from django.urls import path
from .views import get_summary_details, get_summary_text_rank # , get_summary_bert
app_name = 'Summarisation'

urlpatterns = [
    path('text_rank/', get_summary_text_rank),
#    path('bert/', get_summary_bert),
    path('help/',get_summary_details),
]
