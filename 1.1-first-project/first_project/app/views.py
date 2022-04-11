import os

from django.http import HttpResponse
from django.shortcuts import render, reverse
from datetime import datetime


# function returns home page formatted according to home.html
def home_view(request):
    template_name = 'app/home.html'
    pages = {
        'Главная страница': reverse('home'),
        'Показать текущее время': reverse('time'),
        'Показать содержимое рабочей директории': reverse('workdir')
    }

    context = {
        'pages': pages
    }
    return render(request, template_name, context)


# function returns current time
def time_view(request):
    current_time = datetime.now().strftime("%H:%M:%S")
    msg = f'Текущее время: {current_time}'
    print('' + str(os.listdir()))
    return HttpResponse(msg)


# function returns the content of work directory
def workdir_view(request):
    dir_list = os.listdir()
    return HttpResponse('Содержимое рабочей директории: ' + str(dir_list))
