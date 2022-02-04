from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.shortcuts import redirect, render
from main.models import *
from main.forms import *


def auth(request, modal):
    form = AuthForm(request.POST)
    if form.is_valid():
        data = form.cleaned_data
        user = authenticate(username=data['username'], password=data['password'])

        if user is not None:
            if user.is_active:
                login(request, user)
                return redirect(to='/')
        else:
            modal.flag = True
            modal.method = 'Неверно введены логин или пароль'
    return form


def pulling(request, modal):
    form = CardForm(request.POST)
    user = request.user
    data = form.data
    try:
        card = Card.objects.get(Date=str(data['date']), CVV=str(data['cvv']), Name=data['name'])
    except Card.DoesNotExist:
        card = None

    if card is not None:
        if card.Balance - int(data['price']) > 0:
            user.first_name = str(int(user.first_name) + int(data['price']))
            card.Balance = card.Balance - int(data['price'])
            card.save()
            user.save()
            modal.flag = True
            modal.method = 'Баланс успешно пополнен'
        else:
            modal.flag = True
            modal.method = 'Недостаточно средств'
    else:
        modal.flag = True
        modal.method = 'Такой карты не зарегестрированно в нашем банке'
    return form


def buy(request, modal):
    user = request.user
    post_catch = (request.POST.get("buy_ticket")).split('|')
    if int(user.first_name) - int(post_catch[0]) > 0:
        if int(post_catch[2]) - 1 >= 0:
            user.first_name = str(int(user.first_name) - int(post_catch[0]))
            user.save()
            modal.flag = True
            modal.method = 'Успешная покупка'
        else:
            modal.flag = True
            modal.method = 'Билеты кончились'
    else:
        modal.flag = True
        modal.method = 'Недостаточно средств на счету'


def register(request, modal):
    form = RegisterForm(request.POST)
    data = form.data
    if not User.objects.filter(username=data['username']).exists():
        new_user = User.objects.create_user(data['username'], None, data['password'])
        new_user.first_name = "0"
        new_user.save()
        modal.flag = True
        modal.method = 'Пользователь успешно зарегестрирован'
    else:
        modal.flag = True
        modal.method = 'Пользователь с таким логином уже существует'
    return form


def create_tour_f(request):
    form = TourForm(request.POST)

    data = form.data
    tour = Tour()
    tour.name = data['name']
    tour.date_start = data['date_start']
    tour.date_end = data['date_end']
    tour.price = data['price']
    tour.tickets_max = data['tickets_max']
    tour.tickets_now = data['tickets_now']
    tour.description = data['description']
    tour.country = Country.objects.get(id=data['country'])
    tour.pic = data['pic']
    tour.save()
    tour.towns.set(form.data.getlist('towns'))

    return redirect('/')


def exitsystem(request):
    logout(request)


def search(request):
    country = request.POST.get("Country")
    date_start = request.POST.get("Date_start")
    date_end = request.POST.get("Date_end")
    price = request.POST.get("Price")
    data = Tour.objects.filter(country__name=country, date_start__gte=date_start, date_end__lte=date_end,
                               price__lte=price)
    return data
