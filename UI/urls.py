from django.urls import path

from . import views

app_name = 'UI'
urlpatterns = [
        path('', views.index, name='index'),
        path('process', views.handle_common_request, name='summarise')
]
