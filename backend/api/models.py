from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Transactions(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE)  # user is passed in with a foreign key, linking things to specific user
    amount=models.DecimalField(max_digits=10, decimal_places=2)
    transaction_type=models.CharField(max_length=20)
    date=models.DateField()
    description=models.TextField(blank=True)


class Budgets(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE)  # CASCADE means that if User is deleted, all objects assosicated are deleted
    category=models.CharField(max_length=20)
    limit=models.DecimalField(max_digits=10, decimal_places=2)
    period=models.CharField(max_length=20)  # weekly or monthly