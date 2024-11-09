from django.shortcuts import render
from rest_framework.response import Response
from django.contrib.auth.models import User
from rest_framework import generics, permissions  # generics provides class-based views, permissions helps us control access
from .models import Transaction
from .models import Budget
from .serializer import TransactionSerializer
from .serializer import BudgetSeriealizer
from .serializer import UserSerializer


# Create your views here.
# label these
class TransactionListCreate(generics.ListCreateAPIView):  # lets us list & create records in a single view
    ''' 
    List & Create Transactions, user is saved when transaction is created. 
    Listed Transactions are only transactions the user created.
    '''
    # queryset = Transaction.objects.all() is REQUIRED for creating,but behavior will be handled automatically by ListCreateAPIView

    serializer_class = TransactionSerializer  # tells view how to conver Json data to python object (when sending and recieving data)
    permission_classes = [permissions.IsAuthenticated]  # make sure only logged in users can access this view,  standard redundent fail safe

    def get_queryset(self):  # overrides queryset = ...all(), custom filter
        return Transaction.objects.filter(user=self.request.user)  # filter where user field = current authenticated user
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)  # saves the current user from the serializer to user feild in the database


class TransactionRetrieveUpdateDetroy(generics.RetrieveUpdateDestroyAPIView):
    '''
    Update & Delete existing transactions
    '''
    serializer_class=TransactionSerializer
    permission_classes = [permissions.IsAuthenticated]
    #lookup_field = 'pk' ID of Transaction

    def get_queryset(self):  # only logged in user's transactions can be updated/deleted
        return Transaction.objects.filter(user=self.request.user)
    # ^^^ may not be needed, since we can update/delete by primary key(pk) and only ones listed will be current users


class BudgetListCreate(generics.ListCreateAPIView):
    ''' 
    List & Create Budgets, user is saved when Budget is created. 
    Listed Budgets are only transactions the user created.
    '''
    serializer_class = BudgetSeriealizer
    permission_classes = [permissions.IsAuthenticated] 

    def get_queryset(self):
        return Budget.objects.filter(user=self.request.user)
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
    

class BudgetRetrieveUpdateDetroy(generics.RetrieveUpdateDestroyAPIView):
    '''
    Update & Delete existing Budgets
    '''
    serializer_class = BudgetSeriealizer
    permission_classes = [permissions.IsAuthenticated] 
    #lookup_field = 'pk' ID of Budget

    def get_queryset(self):
        return Budget.objects.filter(user=self.request.user)


class UserRegistration(generics.CreateAPIView):
    serializer_class= UserSerializer
    queryset=User.objects.all()


class UserDelete(generics.DetroyAPIView):
    permission_classes = [permissions.IsAuthenticated]

    def delete(self, request):
        user = request.user
        user.delete()
        return Response({"detail": "Account deleted successfully."})
    
# User login (not needed using django's built in authenticator, login handled in urls.py/directly at endpiint)

    
# Dashboard Graph endpoint
# 