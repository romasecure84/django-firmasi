from django.shortcuts import render
from django.http import HttpResponse
from random import randint

def home(request):
    context = {'platform': f'Django Platformu Istifade Edildi: {randint(1, 100)} '}
    return render(request, 'page/home_page.html', context)

