from django.db import models
from datetime import datetime


class Expense(models.Model):
    amount = models.DecimalField(max_digits=10, decimal_places=2)

    CATEGORIES = [
        ('food', 'Food'),
        ('transport', 'Transport'),
        ('bills', 'Bills'),
        ('entertainment', 'Entertainment'),
        ('other', 'Other'),
    ]

    category = models.CharField(max_length=50, choices=CATEGORIES)
    date_and_time = models.DateTimeField(default=datetime.now)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return f'{self.category} - {self.amount}'