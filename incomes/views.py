from django.shortcuts import render, redirect
from .forms import IncomeForm


def add_income(request):
    if request.method == 'POST':
        form = IncomeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = IncomeForm()

    return render(request, 'add_income.html', {'form': form})