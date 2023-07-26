# contracts/forms.py
from django import forms
from .models import Contract

class ContractForm(forms.ModelForm):
    class Meta:
        model = Contract
        fields = ['date', 'place', 'income', 'travel_distance', 'expense', 'invoice_pdf']

        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
        }