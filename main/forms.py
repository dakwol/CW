from django import forms
from main.models import *


class CardForm(forms.Form):
    name = forms.CharField(widget=forms.NumberInput(attrs={'id': 'name', 'type': 'text', 'class': 'card__inp', 'maxlength': '20'}))
    date = forms.IntegerField(widget=forms.NumberInput(attrs={'id': 'expirationdate', 'type': 'text', 'class': 'card__inp'}))
    cvv = forms.IntegerField(widget=forms.NumberInput(attrs={'id': 'securitycode', 'type': 'text', 'class': 'card__inp'}))
    price = forms.IntegerField(widget=forms.NumberInput(attrs={'id': 'prycecode', 'type': 'text', 'class': 'card__inp'}))


class SearchForm(forms.Form):
    Country = forms.CharField()
    Date_start = forms.DateField()
    Date_end = forms.DateField()
    Price = forms.IntegerField()


class AuthForm(forms.Form):
    username = forms.CharField(max_length=50, label='Имя пользователя')
    password = forms.CharField(max_length=50, label='Пароль', widget=forms.PasswordInput)


class RegisterForm(forms.Form):
    username = forms.CharField(max_length=50, label='Имя пользователя')
    password = forms.CharField(max_length=50, label='Пароль', widget=forms.PasswordInput)


class TourForm(forms.ModelForm):
    class Meta:
        model = Tour
        fields = ['name', 'date_start', 'date_end', 'price', 'tickets_max', 'tickets_now', 'description', 'country',
                  'towns', 'pic']

    name = forms.CharField()
    date_start = forms.DateField()
    date_end = forms.DateField()
    price = forms.IntegerField()
    tickets_max = forms.IntegerField()
    tickets_now = forms.IntegerField()
    description = forms.CharField()
    country = forms.ModelChoiceField(queryset=Country.objects.all())
    towns = forms.ModelMultipleChoiceField(queryset=Town.objects.none(), widget=forms.CheckboxSelectMultiple)
    pic = forms.CharField()


class Modal_Window:
    flag = False
    method = ''
