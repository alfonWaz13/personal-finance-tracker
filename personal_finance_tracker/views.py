from django.shortcuts import render

from expenses.models import Expense
from incomes.models import Income

def dashboard(request):
    expenses = get_expenses()
    incomes = get_incomes()

    total_balance = get_total_balance(expenses, incomes)

    context = {
        'expenses': expenses,
        'incomes': incomes,
        'total_balance': total_balance,
    }

    return render(request, 'dashboard.html', context)


def get_total_balance(expenses, incomes):
    total_expenses = sum(expense.amount for expense in expenses)
    total_incomes = sum(income.amount for income in incomes)
    total_balance = total_incomes - total_expenses
    return total_balance


def get_incomes():
    return Income.objects.all().order_by('-date_and_time')


def get_expenses():
    return Expense.objects.all().order_by('-date_and_time')
