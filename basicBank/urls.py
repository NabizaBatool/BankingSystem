from django.urls import path
from . import views

urlpatterns = [
    path('',views.index, name= 'index'),
    path('customers/',views.customerDetails, name= 'customers'),
    path('transactionDetail/',views.transactionDetails, name= 'transactionDetail'),
    path('transferMoney/',views.transferMoney, name= 'transferMoney'),
]