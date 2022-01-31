from django.http import HttpResponse
# from django.shortcuts import render
# from django.shortcuts import render, redirect


# Create your views here.
from django.shortcuts import render


def index(request):
    return render(request, 'base.html')
