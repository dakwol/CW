import datetime
from django.shortcuts import render
from main.Functions import *
from main.forms import *


# Create your views here.


def index(request):
    search_form = SearchForm()
    register_form = RegisterForm()
    auth_form = AuthForm()
    data = Tour.objects.filter(date_start__gte=datetime.date.today())
    card_form = CardForm()

    if request.method == "POST":
        if request.POST.get('exit'):
            exitsystem(request)
        if request.POST.get("filter"):
            data = search(request)
        if request.POST.get("buy_ticket"):
            buy(request)
        if request.POST.get("register"):
            register_form = register(request)
        if request.POST.get("login"):
            auth_form = auth(request)
        if request.POST.get("pulling"):
            pulling(request)

    return render(request, 'main.html', {'data': data, 'sf': search_form, 'authform': auth_form,
                                         'regform': register_form,
                                         'user': request.user,
                                         'card_form': card_form})


def create_tour(request):
    return render(request, 'admin.html')
