from django import forms
from .models import Expense

class ExpenseForm(forms.ModelForm):
    class Meta:
        model = Expense
        fields = ['date', 'description', 'amount', 'receipt', 'is_travel_allowance', 'travel_distance']

        widgets = {
                'date': forms.DateInput(attrs={'type': 'date'}),
            }

    # Custom labels for the fields
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['is_travel_allowance'].label = 'Allowance'
        self.fields['travel_distance'].label = 'Distance'