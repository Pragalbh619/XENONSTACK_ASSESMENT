from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User,auth
from django.core.mail import send_mail
from django.contrib.auth.hashers import make_password
from administrator.models import product, purchase
import os
from django.core.files.storage import FileSystemStorage



def home(request):
    k=product.objects.all()
    
    return render(request,'front/home.html',{'data':k})

def query(request):
    return render(request,'front/query.html')


def query_table(request):
    first_name=request.POST['first_name']
    last_name=request.POST['last_name']
    subject=request.POST['subject']
    country=request.POST['country']

    return redirect("home")
    
def product_details(request):
    id = request.GET['id']
    data = product.objects.get(pk=id)
    return render(request,'front/pd.html',{'data':data})

def pd(request):
    return render(request,'front/pd.html')


def  reviews_save(request):
    name=request.POST['name']
    email=request.POST['email']
    review=request.POST['review']
    
    k = User.objects.create_user(name=name,email=email,review=review)
    k.save()
    return redirect("")

def shop(request):
    k = product.objects.all()
    return render(request,'front/shop.html',{'data':k})

def checkout(request):
    id = request.GET['id']
    data = product.objects.get(pk=id)
    return render(request,'front/checkout.html',{'data':data})

def purchase1(request):
   c_name = request.POST['c_name']
   p_name = request.POST['p_name']
   p_price = request.POST['p_price']
   email = request.POST['email']
   state=request.POST['state']
   city=request.POST['city']
   address = request.POST['address']
   pay_method = request.POST['pay_method']
   if(pay_method=="COD"):
       k = purchase(category=c_name,product=p_name,price=p_price,emails=email,state=state,city=city,address=address)
       k.save()
       
       #email 
       
       
       
       
       return render(request,'front/thankyou.html',{'data':'Thanks! Your Order has been received. We shall get back to you asap!'})
   else:
       #return HttpResponse(c_name+p_name)
       k = purchase(category=c_name, product=p_name, price=p_price,emails=email,state=state,city=city,address=address)
       k.save()
       #code for online payment - integrated but do not have merchant key.
       return render(request,'front/thankyou.html',{'data':'Thanks! Your Order has been received. We shall get back to you asap!'})
       


def faq(request):
    return render(request,'front/faq.html') 