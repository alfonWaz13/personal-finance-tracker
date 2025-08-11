from django import forms
from .models import Expense

class ExpenseForm(forms.ModelForm):
    class Meta:
        model = Expense
        fields = ['amount', 'category', 'date_and_time', 'description']
        widgets = {
            'date_and_time': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        }