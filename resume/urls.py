from django.urls import path
from resume.views import home

app_name = 'resume'


urlpatterns = [
    path('',home,name='home'),
]