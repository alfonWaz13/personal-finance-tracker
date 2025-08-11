from django.shortcuts import render

from expenses.models import Expense
from incomes.models import Income


def homepage(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')


def dashboard(request):
    expenses = Expense.objects.all().order_by('-date_and_time')
    incomes = Income.objects.all().order_by('-date_and_time')

    context = {
        'expenses': expenses,
        'incomes': incomes,
    }

    return render(request, 'dashboard.html', context)
