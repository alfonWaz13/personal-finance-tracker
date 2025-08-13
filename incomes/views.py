from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from .forms import IncomeForm
from .models import Income


def add_income(request):
    if request.method == 'POST':
        form = IncomeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = IncomeForm()

    return render(request, 'add_income.html', {'form': form})


@require_POST
def delete_income(_, pk):
    income = get_object_or_404(Income, pk=pk)
    income.delete()
    return redirect('dashboard')