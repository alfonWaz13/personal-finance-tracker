from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from .forms import ExpenseForm
from .models import Expense


def add_expense(request):
    if request.method == 'POST':
        form = ExpenseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = ExpenseForm()

    return render(request, 'add_expense.html', {'form': form})


@require_POST
def delete_expense(_, pk):
    expense = get_object_or_404(Expense, pk=pk)
    expense.delete()
    return redirect('dashboard')