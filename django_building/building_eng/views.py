from django.shortcuts import render, redirect, HttpResponseRedirect, reverse
from django.views import View
from django.contrib import messages
from .models import EnProject, EnOldProject, EnVacancy
from .forms import EnContactForm, EnNewEmployeeForm
import requests
from .config import token, chat_id


class EnMainPageView(View):
    def get(self, request):
        form = EnContactForm
        projects = EnProject.objects.all()
        old_projects = EnOldProject.objects.all()
        context = {
            "title": 'TTConsulting',
            "form": form,
            "projects": projects,
            "old_projects": old_projects
        }
        return render(request, 'en_main.html', context)


class EnSendMessage(View):

    def post(self, request):
        form = EnContactForm(request.POST)

        if form.is_valid():
            try:
                auth = form.cleaned_data['first_name']
                phone = form.cleaned_data['phone']
                email = form.cleaned_data['email']
                message = form.cleaned_data['message']
                msg = f'TTCONSULTING: Свяжитесь со мной\n\n' \
                      f'автор: {auth}\n' \
                      f'телефон: {phone}\n' \
                      f'email: {email}\n' \
                      f'сообщение: \n\n' \
                      f'"{message}"'
                requests.get(f'https://api.telegram.org/bot{token}/sendMessage?chat_id={chat_id}&text={msg}')

                form.save()
                messages.success(request, 'ваше сообщение было отправлено')
                return HttpResponseRedirect(reverse('en:main'))

            except ValueError:
                messages.error(request, 'форма была заполнена неправильно')
                return HttpResponseRedirect(reverse('en:main'))

        messages.error(request, 'форма была заполнена неправильно')
        return HttpResponseRedirect(reverse('en:main'))


class EnVacanciesView(View):

    def get(self, request):
        form = EnNewEmployeeForm
        vacancies = EnVacancy.objects.all()
        context = {
            'title': 'TTC Vacancy ',
            'form': form,
            'vacancies': vacancies
        }
        return render(request, 'en_vacancies.html', context)


class EnSendBid(View):

    def post(self, request):
        form = EnNewEmployeeForm(request.POST)

        if form.is_valid():
            try:
                # tg msg
                position = form.cleaned_data['position']
                first_name = form.cleaned_data['first_name']
                last_name = form.cleaned_data['last_name']
                phone = form.cleaned_data['phone']
                year = form.cleaned_data['year']
                location = form.cleaned_data['location']

                msg = f"Вакансия: {position}\n\n" \
                      f"кандидат: {first_name} {last_name}\n" \
                      f"год рождения: {year}\n" \
                      f"телефон: {phone}\n" \
                      f"местоположение: {location}"
                requests.get(f'https://api.telegram.org/bot{token}/sendMessage?chat_id={chat_id}&text={msg}')
                form.save()
                messages.success(request, 'ваша заявка отправлена')
                return HttpResponseRedirect(reverse('en:main'))

            except ValueError:
                messages.error(request, 'форма была заполнена неправильно')
                return HttpResponseRedirect(reverse('en:vacancies'))

        messages.error(request, 'форма была заполнена неправильно')
        return HttpResponseRedirect(reverse('en:vacancies'))
