from rest_framework import serializers
from .models import (Transaction, Budget)

# take models and convert them to Json compatitible data and vice versa
class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model=Transaction
        fields= '__all__'

class BudgetSeriealizer(serializers.ModelSerializer):
    class Meta:
        mode=Budget
        fields= '__all__'

