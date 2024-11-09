from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Transaction(models.Model):
    # inputs that go into table
    CLOTHING = 'CLO'
    MISCELLANEOUS = 'MISC'
    FOOD = 'FOOD'
    HOUSING = 'HOUS'
    LEISURE = 'LEIS'
    
    # transaction times that will appear in drop down and their mapping, human readable text :  
    TRANSACTION_TYPES = {
        CLOTHING: 'Clothing',
        MISCELLANEOUS: 'Miscellaneous',
        FOOD: 'Food',
        HOUSING: 'Housing',
        LEISURE: 'Leisure',
    }
    # are called fields
    user=models.ForeignKey(User, on_delete=models.CASCADE)  # user is passed in with a foreign key, linking things to specific user
    amount=models.DecimalField(max_digits=10, decimal_places=2)
    transaction_type=models.CharField(
        max_length=4,
        choices = TRANSACTION_TYPES,
        )
    date=models.DateTimeField(
        auto_now_add=True,
        editable=False,
        )  # automatic inputs the date and time of transaction
    description=models.TextField(blank=True)


class Budget(models.Model):
    CLOTHING = 'CLO'
    MISCELLANEOUS = 'MISC'
    FOOD = 'FOOD'
    HOUSING = 'HOUS'
    LEISURE = 'LEIS'

    BUDGET_TYPES = {
        CLOTHING: 'Clothing',
        MISCELLANEOUS: 'Miscellaneous',
        FOOD: 'Food',
        HOUSING: 'Housing',
        LEISURE: 'Leisure',
    }

    user=models.ForeignKey(User, on_delete=models.CASCADE)  # CASCADE means that if User is deleted, all objects assosicated are deleted
    category=models.CharField(
        max_length=4,
        choices = BUDGET_TYPES,
        )
    limit=models.DecimalField(max_digits=10, decimal_places=2)
    period=models.CharField(max_length=20)  # weekly or monthly