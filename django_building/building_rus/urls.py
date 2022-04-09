from django.urls import path
from .views import *

urlpatterns = [
    path('', RuMainPageView.as_view(), name='main'),
    path('vacancies/', RuVacanciesView.as_view(), name='vacancies'),
    path('contact-form/', RuSendMessage.as_view(), name='contact-form'),
    path('vacancies-form/', RuSendBid.as_view(), name='vacancies-form'),
]