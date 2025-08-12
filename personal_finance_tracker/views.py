from django.shortcuts import render

from expenses.models import Expense
from incomes.models import Income

def dashboard(request):
    expenses = Expense.objects.all().order_by('-date_and_time')
    incomes = Income.objects.all().order_by('-date_and_time')

    total_expenses = sum(expense.amount for expense in expenses)
    total_incomes = sum(income.amount for income in incomes)
    total_balance = total_incomes - total_expenses

    context = {
        'expenses': expenses,
        'incomes': incomes,
        'total_balance': total_balance,
    }

    return render(request, 'dashboard.html', context)
