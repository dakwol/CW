from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect
from main.models import *
from main.forms import *


def auth(request):
    form = AuthForm(request.POST)

    if form.is_valid():
        data = form.cleaned_data
        user = authenticate(username=data['username'], password=data['password'])

        if user is not None:
            if user.is_active:
                login(request, user)
                return redirect(to='/')
    return form


def pulling(request):
    form = CardForm(request.POST)
    user = request.user
    data = form.data
    card = Card.objects.get(Date=str(data['date']), CVV=str(data['cvv']), Name=data['name'])
    if card is not None:
        if card.Balance - int(data['price']) > 0:
            user.first_name = str(int(user.first_name) + int(data['price']))
            card.Balance = card.Balance - int(data['price'])
            card.save()
            user.save()
            return redirect(to='/')
    return form


def buy(request):
    user = request.user
    post_catch = (request.POST.get("buy_ticket")).split('|')
    if int(user.first_name) - int(post_catch[0]) > 0 and int(post_catch[2]) - 1 >= 0:
        user.first_name = str(int(user.first_name) - int(post_catch[0]))
        user.save()


def register(request):
    form = RegisterForm(request.POST)
    if request.POST.get('register'):
        data = form.data
        if not User.objects.filter(username=data['username']).exists():
            new_user = User.objects.create_user(data['username'], None, data['password'])
            new_user.first_name = "0"
            new_user.save()
            return redirect(to='/')
    return form


def exitsystem(request):
    logout(request)


def search(request):
    country = request.POST.get("Country")
    date_start = request.POST.get("Date_start")
    date_end = request.POST.get("Date_end")
    price = request.POST.get("Price")
    data = Tour.objects.filter(country__name=country, date_start__gte=date_start, date_end__lte=date_end, price__lte=price)
    return data

