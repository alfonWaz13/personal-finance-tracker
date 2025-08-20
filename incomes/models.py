from django.db import models
from datetime import datetime

class Income(models.Model):
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    CATEGORIES = [
        ('salary', 'Salary 💵'),
        ('investment', 'Investment 📈'),
        ('gift', 'Gift 🎁'),
        ('other', 'Other 💼'),
    ]

    category = models.CharField(max_length=50, choices=CATEGORIES)
    date_and_time = models.DateTimeField(default=datetime.now)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return f'{self.category} - {self.amount}'