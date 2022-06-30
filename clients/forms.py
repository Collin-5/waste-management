from django import forms
from .models import Clients

class ClientAddForm(forms.ModelForm):
    # first_name = forms.CharField(
    #     widget=forms.TextInput(
    #         attrs={
    #             "placeholder": "first_name",
    #             "class": "form-control"
    #         }
    #     ))

    # last_name = forms.CharField(
    #     widget=forms.TextInput(
    #         attrs={
    #             "placeholder": "last_name",
    #             "class": "form-control"
    #         }
    #     ))
    # phone = forms.IntegerField(
    #     widget=forms.NumberInput(
    #         attrs={
    #             "placeholder": "+254..",
    #             "class": "form-control"
    #         }
    #     ))

    # email = forms.EmailField(
    #     widget=forms.EmailInput(
    #         attrs={
    #             "placeholder": "Email",
    #             "class": "form-control"
    #         }
    #     ))

    # address = forms.CharField(
    #     widget=forms.TextInput(
    #         attrs={
    #             "placeholder": "address",
    #             "class": "form-control"
    #         }
    #     ))
    # waste_type = forms.CharField(
    #     widget=forms.Select(
    #         # choices=[
    #         #         ('LIQUID WASTE','liquid waste'),
    #         #         ('SOLID WASTE','solid waste'),
    #         #         ('ORGANIC WASTE','Organic Waste'),
    #         #         ('RECYCLABLE WASTE','Recyclable Rubbish'),
    #         #         ('HAZARDOUS WASTE','Hazardous Waste')
    #         #     ],
    #         attrs={
    #             "placeholder": "waste_type",
    #             "class": "form-control",
                
    #         }
    #     ))
    # number_of_bins = forms.IntegerField(
    #     widget=forms.NumberInput(
    #         attrs={
    #             "placeholder": "0",
    #             "class": "form-control"
    #         }
    #     ))

    class Meta:
        model = Clients
        fields = ('first_name', 'last_name', 'email', 'Address', 'phone', 'waste_type', 'number_of_bins')