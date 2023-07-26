# expenses/forms.py
from django import forms
from .models import OperatingExpense

class OperatingExpenseForm(forms.ModelForm):
    class Meta:
        model = OperatingExpense
        fields = ['date', 'hours_worked', 'federal_tax', 'provincial_tax', 'cpp', 'ei', 'employee']

        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
        }