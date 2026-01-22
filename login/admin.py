from django.contrib import admin
from . import models

@admin.register(models.Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ['name', 'last_name', 'email', 'date_en']
    search_fields = ['name__istartswith', 'last_name__istartswith']