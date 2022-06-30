from email.headerregistry import Address
from django.db import models
from django.contrib.auth import get_user_model
import random
import uuid

# Create your models here.

CHOICES = [
    ('LIQUID WASTE','liquid waste'),
    ('SOLID WASTE','solid waste'),
    ('ORGANIC WASTE','Organic Waste'),
    ('RECYCLABLE WASTE','Recyclable Rubbish'),
    ('HAZARDOUS WASTE','Hazardous Waste')
]

class Clients(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    Address = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    waste_type = models.CharField(max_length=100, choices=CHOICES)
    number_of_bins = models.IntegerField()
    status = models.BooleanField(default=False)


def random_string():
    return str(random.randint(10000000, 99999999))

class Invoice(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    client = models.ForeignKey(get_user_model(), on_delete=models.PROTECT)
    details = models.TextField(null=True, blank=True)
    amount = models.IntegerField(null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True)
    date_due = models.DateField(null=True, blank=True)
    invoice_no = models.CharField(max_length=8, default=random_string(), editable=False)
    status = models.BooleanField(default=False)