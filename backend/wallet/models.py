from django.db import models
from django.contrib.auth.models import User


class Transaction(models.Model):

    TYPE_CHOICES = (
        ('Income', 'Income'),
        ('Expense', 'Expense'),
    )

    CATEGORY_CHOICES = (
        ('Food', 'Food'),
        ('Travel', 'Travel'),
        ('Shopping', 'Shopping'),
        ('Salary', 'Salary'),
        ('Bills', 'Bills'),
        ('Other', 'Other'),
    )

    user = models.ForeignKey(User, on_delete=models.CASCADE)

    title = models.CharField(max_length=100)

    amount = models.IntegerField()

    transaction_type = models.CharField(
        max_length=20,
        choices=TYPE_CHOICES
    )

    category = models.CharField(
        max_length=50,
        choices=CATEGORY_CHOICES
    )

    created_at = models.DateField(auto_now_add=True)

    def __str__(self):

        return self.title