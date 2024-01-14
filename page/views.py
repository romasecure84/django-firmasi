from django.shortcuts import render
from django.http import HttpResponse
from random import randint

def home_view(request):
    # context = {'platform': f'Django Platformu Istifade Edildi: {randint(1, 100)} '}
    page_title = 'Ana Sehife'
    context = dict(page_title = page_title)
    return render(request, 'page/home_page.html', context)

def about_us_view(request):
    page_title = 'Haqqimizda'
    context = dict(page_title = page_title,)
    return render(request, 'page/about_us_view.html', context)

def contact_us_view(request):
    page_title = 'Elaqe'
    context = dict(page_title = page_title,)
    return render(request, 'page/contact_us_view.html', context)

def vision_view(request):
    page_title = 'Vizyonumuz'
    context = dict(page_title = page_title,)
    return render(request, 'page/vision.html', context)
