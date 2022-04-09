from django.urls import path
from .views import *

urlpatterns = [
    path('', EnMainPageView.as_view(), name='main'),
    path('vacancies/', EnVacanciesView.as_view(), name='vacancies'),
    path('contact-form/', EnSendMessage.as_view(), name='contact-form'),
    path('vacancies-form/', EnSendBid.as_view(), name='vacancies-form'),
]