from django.urls import path
from . import views  # imported whole file, access specific views with views.className/function
from rest_framework.authtoken.views import obtain_auth_token
from django.contrib.auth import views as auth_views

urlpatterns=[  #path('URL sting path', views.{view_name}, nameForUrl)
    path('account/register', views.UserRegistration.as_view(), name='register'),  # .as_view() is neccessay for class based views, not function based views
    path('account/login', obtain_auth_token, name='login'),
    path('account/delete', views.UserDelete.as_view(), name='delete'),
    # built in password change views endpoints
    path('password_change/', auth_views.PasswordChangeView.as_view(), name='password_change'),
    path('password_change/done/', auth_views.PasswordChangeDoneView.as_view(), name='password_change_done'),
    
    path('/transactions', views.TransactionListCreate.as_view(), name='transactions'),
    path('transactions/edit', views.TransactionRetrieveUpdateDetroy.as_view(), name='edit_transactions'),
    path('budgets', views.BudgetListCreate.as_view(), name='budget'),
    path('budgets/edit', views.BudgetRetrieveUpdateDetroy.as_view(), name='edit_budget'),
]