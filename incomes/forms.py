from django import forms
from .models import Income

class IncomeForm(forms.ModelForm):
    class Meta:
        model = Income
        fields = ['amount', 'category', 'date_and_time', 'description']
        widgets = {
            'date_and_time': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        }