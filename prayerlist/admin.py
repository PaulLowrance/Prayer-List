from django.contrib import admin
from .models import PrayerType, Request
# Register your models here.

admin.site.register(PrayerType)
admin.site.register(Request)