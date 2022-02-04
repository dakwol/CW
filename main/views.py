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
    modal = Modal_Window

    if request.method == "POST":
        if request.POST.get('Ok'):
            modal.flag = False

        if request.POST.get('exit'):
            exitsystem(request)
        if request.POST.get("filter"):
            data = search(request)
        if request.POST.get("buy_ticket"):
            buy(request, modal)
        if request.POST.get("register"):
            register_form = register(request, modal)
        if request.POST.get("login"):
            auth_form = auth(request, modal)
        if request.POST.get("pulling"):
            pulling(request, modal)

    return render(request, 'main.html', {'data': data, 'sf': search_form, 'authform': auth_form,
                                         'regform': register_form,
                                         'user': request.user,
                                         'card_form': card_form,
                                         'modal': modal})


def create_tour(request):
    form = TourForm(request.POST)
    show_button = True
    if request.method == "POST":
        show_button = True
        if request.POST.get("Show_towns"):
            country = request.POST.get("country")
            form.fields['towns'].queryset = Town.objects.filter(country=country)
            show_button = False
        if request.POST.get("create"):
            form = create_tour_f(request)

    return render(request, 'admin.html', {'form': form, 'show_button': show_button})
