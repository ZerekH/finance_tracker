from rest_framework import serializers
from .models import (Transaction, Budget)
from django.contrib.auth.models import User

# take models and convert them to Json compatitible data and vice versa
class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = '__all__'  # include all fields, Id is auto generated

        extra_kwargs = {
            'amount': {'required': True},
            'date': {'required': True},
            'transaction_type': {'required': True},
        }

class BudgetSeriealizer(serializers.ModelSerializer):
    class Meta:
        model = Budget
        fields = '__all__'

        extra_kwargs = {
            'limit': {'required': True},  # budget imit is required
            'category': {'required': True},
        }

class UserSerializer(serializers.User):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ('username', 'email', 'password', 'first_name', 'last_name')

        extra_kwargs = {
            'password': {'write_only': True},  # Make sure password is write-only
            'email': {'required': True},  # Make email required
            'first_name': {'required': True},  # Make first name required
            'last_name': {'required': True},  # Make last name required
        }
    # The create function in the serializer is typically only needed when 
    # you need to modify the saving behavior 
    #(e.g., hashing passwords, adding custom fields, or additional validation).
    def create(self, validated_data): # validated_data contains the data that was passed in by the client but has been cleaned up and validated
        user = User(
            username=validated_data['username'],
            email=validated_data['email'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
        )
        # reason we used a create function:
        # set_password hashes the users password so it is not stored in plain text
        user.set_password(validated_data['password'])  # Password hashing needs to happen after the User object is created, but before saving it to the database.
        user.save()
        return user