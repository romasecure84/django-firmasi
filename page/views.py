from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return HttpResponse('Ana Sehifeye Xos Geldiniz!')
# Create your views here.
