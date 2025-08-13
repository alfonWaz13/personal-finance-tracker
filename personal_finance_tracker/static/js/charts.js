document.addEventListener('DOMContentLoaded', function() {
    const expenseDataElement = document.getElementById('expense-data');
    const incomeDataElement = document.getElementById('income-data');

    if (!expenseDataElement || !incomeDataElement) {
        return;
    }

    const expenseData = JSON.parse(expenseDataElement.textContent);
    const incomeData = JSON.parse(incomeDataElement.textContent);

    const expenseLabels = expenseData.map(item => item.category);
    const expenseTotals = expenseData.map(item => item.total);

    const incomeLabels = incomeData.map(item => item.category);
    const incomeTotals = incomeData.map(item => item.total);

    // Predefined colors for expenses and incomes
    const expenseColors = [
        '#FF6384', '#36A2EB', '#FFCE56', '#4BC0C0', '#9966FF', '#FF9F40'
    ];
    const incomeColors = [
        '#4BC0C0', '#9966FF', '#FF9F40', '#FF6384', '#36A2EB', '#FFCE56'
    ];

    const expenseCtx = document.getElementById('expenseChart').getContext('2d');
    new Chart(expenseCtx, {
        type: 'pie',
        data: {
            labels: expenseLabels,
            datasets: [{
                label: 'Expense by Category',
                data: expenseTotals,
                backgroundColor: expenseColors,
            }]
        },
        options: {
            responsive: false,
            maintainAspectRatio: false,
            plugins: {
                legend: {
                    position: 'top',
                },
                title: {
                    display: false,
                }
            },
            cutout: '70%'
        },
    });

    const incomeCtx = document.getElementById('incomeChart').getContext('2d');
    new Chart(incomeCtx, {
        type: 'pie',
        data: {
            labels: incomeLabels,
            datasets: [{
                label: 'Income by Category',
                data: incomeTotals,
                backgroundColor: incomeColors,
            }]
        },
        options: {
            responsive: false,
            maintainAspectRatio: false,
            plugins: {
                legend: {
                    position: 'top',
                },
                title: {
                    display: false,
                }
            },
            cutout: '70%'
        },
    });
});
