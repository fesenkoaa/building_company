from django.shortcuts import render, redirect
from django.views import View
from django.contrib import messages
from .models import Project, OldProject, Vacancy
from .forms import ContactForm, NewEmployeeForm
import requests
from .config import token, chat_id


class MainPageView(View):
    def get(self, request):
        form = ContactForm
        projects = Project.objects.all()
        old_projects = OldProject.objects.all()
        context = {
            "title": 'TTConsulting',
            "form": form,
            "projects": projects,
            "old_projects": old_projects
        }
        return render(request, 'main.html', context)


class SendMessage(View):

    def post(self, request):
        form = ContactForm(request.POST)

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
                return redirect('main')

            except ValueError:
                messages.error(request, 'форма была заполнена неправильно')
                return redirect('main')

        messages.error(request, 'форма была заполнена неправильно')
        return redirect('main')


class GalleryPage(View):

    def get(self, request):
        context = {
            'title': 'TTC Gallery',
        }
        return render(request, 'gallery.html', context)


class VacanciesView(View):

    def get(self, request):
        form = NewEmployeeForm
        vacancies = Vacancy.objects.all()
        context = {
            'title': 'TTC Vacancy ',
            'form': form,
            'vacancies': vacancies
        }
        return render(request, 'vacancies.html', context)


class SendBid(View):

    def post(self, request):
        form = NewEmployeeForm(request.POST)

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
                return redirect('main')

            except ValueError:
                messages.error(request, 'форма была заполнена неправильно')
                return redirect('vacancies')

        messages.error(request, 'форма была заполнена неправильно')
        return redirect('vacancies')
