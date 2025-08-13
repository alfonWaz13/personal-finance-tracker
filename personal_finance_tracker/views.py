from django.shortcuts import render
from django.db.models import Sum

from expenses.models import Expense
from incomes.models import Income

def dashboard(request):
    expenses = get_expenses()
    incomes = get_incomes()

    total_balance = get_total_balance(expenses, incomes)

    expense_by_category = get_entries_by_category(expenses)
    income_by_category = get_entries_by_category(incomes)

    context = {
        'expenses': expenses,
        'incomes': incomes,
        'total_balance': total_balance,
        'expense_by_category': expense_by_category,
        'income_by_category': income_by_category,
    }

    return render(request, 'dashboard.html', context)


def get_entries_by_category(entries: Expense | Income) -> list:
    return list(entries.order_by().values('category').annotate(total=Sum('amount')))


def get_total_balance(expenses, incomes):
    total_expenses = sum(expense.amount for expense in expenses)
    total_incomes = sum(income.amount for income in incomes)
    total_balance = total_incomes - total_expenses
    return total_balance


def get_incomes():
    return Income.objects.all().order_by('-date_and_time')


def get_expenses():
    return Expense.objects.all().order_by('-date_and_time')
