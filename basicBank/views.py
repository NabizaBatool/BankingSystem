from django.shortcuts import render , redirect
from django.contrib import messages

from basicBank.models import *

# Create your views here.
def index(request):
    return render(request, 'index.html')

def customerDetails(request):
    customer = CustomerDetail.objects.all()
    return render(request,'customers.html',{'customer':customer})

def transactionDetails(request):
    transaction=TransactionDetail.objects.all()
    return render(request , 'transactionDetail.html' , {'transaction' : transaction})
def transferMoney(request):
    customer = CustomerDetail.objects.all()
    if request.method=="POST":
        senderEmail=request.POST.get("senderEmail")
        recieverEmail = request.POST.get('recieverEmail')
        amount=request.POST.get("amount")
        amount=int(amount)
        if senderEmail == 'select' or recieverEmail == 'select' or (senderEmail=='select' and recieverEmail=='select') or recieverEmail==senderEmail:
            messages.warning(request,"EmailId not selected or both EmailId's are same")  
        elif amount <= 0:
            messages.warning(request,'Please provide valid money details!!')
        else:
            for cust in customer:
                if cust.email==senderEmail:
                    if amount> cust.currentBalance:
                        messages.warning(request,"Insufficient Balance!!") 
                    else:
                        sendAm=cust.currentBalance-amount 
                        for x in customer:
                            if x.email==recieverEmail:
                                recName=x.name
                                recId=x.id
                                recAm=x.currentBalance+amount
                            continue
                        q3= CustomerDetail.objects.filter(id=recId).update(currentBalance=recAm)
                        q2= CustomerDetail.objects.filter(id=cust.id).update(currentBalance=sendAm)
                        q1= TransactionDetail(sender=cust.name,reciever=recName,amount=amount)
                        q1.save()
                        messages.success(request,"Transfer complete!!")
                        return redirect('transactionDetail')
                
                        

    return render(request,'transferMoney.html',{'customer':customer})
