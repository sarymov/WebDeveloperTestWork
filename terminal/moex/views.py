from django.shortcuts import render
from django.http import HttpResponse


# Главная страница
def index(request):
    template = 'moex/index.html'
    return render(request, template)


def moex_list(request):
    template = 'moex/moex.html'
    return render(request, template)


def group_companies(request):
    return HttpResponse('Список мороженого')


# Страница с информацией об одном сорте мороженого;
# view-функция принимает параметр pk из path()
def moex_detail(request, pk):
    return HttpResponse(f'Мороженое номер {pk}')
