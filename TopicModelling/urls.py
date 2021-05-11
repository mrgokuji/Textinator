from django.urls import path
from .views import get_lda_topics
from .views import get_lsa_topics
app_name = 'TopicModelling'

urlpatterns = [
    path('lda/', get_lda_topics),
    path('lsa/', get_lsa_topics),
]
