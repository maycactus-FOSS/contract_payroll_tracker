# expenses/forms.py
from django import forms
from .models import PayrollExpense

class PayrollExpenseForm(forms.ModelForm):
    class Meta:
        model = PayrollExpense
        fields = ['date', 'hours_worked', 'federal_tax', 'provincial_tax', 'cpp', 'ei', 'employee']

        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
        }