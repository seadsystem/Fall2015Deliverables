from django.contrib import admin

from .models import Table

# Register your models here.
class Listy(admin.ModelAdmin):
    list_display = ('date_time', 'use')


admin.site.register(Table, Listy)
