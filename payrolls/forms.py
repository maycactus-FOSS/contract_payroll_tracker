# expenses/forms.py
from django import forms
from .models import PayrollExpense

class PayrollExpenseForm(forms.ModelForm):
    class Meta:
        model = PayrollExpense
        fields = ['date', 'employee', 'hours_worked', 'federal_tax', 'provincial_tax', 'cpp', 'ei']

        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
        }