from django.urls import path
from .views import get_lda_title
from .views import get_lsa_title
app_name = 'Titling'

urlpatterns = [
    path('lda/', get_lda_title),
    path('lsa/', get_lsa_title),
]
