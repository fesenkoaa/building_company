from django.urls import path
from .views import *

urlpatterns = [
    path('main/', MainPageView.as_view(), name='main'),
    path('gallery/', GalleryPage.as_view(), name='gallery'),
    path('vacancies/', VacanciesView.as_view(), name='vacancies'),
    path('contact-form/', SendMessage.as_view(), name='contact-form'),
    path('vacancies-form/', SendBid.as_view(), name='vacancies-form'),
]