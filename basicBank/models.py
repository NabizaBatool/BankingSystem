from django.db import models

# Create your models here.
class CustomerDetail(models.Model):
    id=models.AutoField(primary_key=True)
    name = models.CharField(max_length=30 , null=True)
    email = models.EmailField(max_length=30 , null=True)
    currentBalance = models.IntegerField()
    def __str__(self):
        return self.name
class TransactionDetail(models.Model):
    sender = models.CharField(max_length=200, null=True)
    reciever = models.CharField(max_length=200, null=True)
    amount = models.IntegerField(default=0)
    date_tran = models.DateTimeField(auto_now_add=True)