from django.contrib import admin

# Register your models here.
from main.models import *

admin.site.register(Country)
admin.site.register(Town)
admin.site.register(Tour)
admin.site.register(Card)
