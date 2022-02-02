from django.http import HttpResponse
# from django.shortcuts import render

from tours.models import *
# Create your views here.
from django.shortcuts import render


def index(request):
    data = Tour.objects.all()
    return render(request, 'main.html', {'data': data})


def about_us(request):
    return render(request, 'base.html')
