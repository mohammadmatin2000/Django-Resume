from django.urls import path
from resume.views import *
app_name = 'resume'
urlpatterns = [
    path('index/',index,name='index'),
]