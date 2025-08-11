from django.shortcuts import render

from expenses.models import Expense
from incomes.models import Income

def dashboard(request):
    expenses = Expense.objects.all().order_by('-date_and_time')
    incomes = Income.objects.all().order_by('-date_and_time')

    context = {
        'expenses': expenses,
        'incomes': incomes,
    }

    return render(request, 'dashboard.html', context)
