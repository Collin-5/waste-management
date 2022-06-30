from django.contrib import admin
from .models import Clients, Invoice
models = [Clients, Invoice]

# Register your models here.
admin.site.register(models)
