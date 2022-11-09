from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User,auth
from django.core.mail import send_mail
from django.contrib.auth.hashers import make_password
from.models import category,purchase,product
import os
from django.core.files.storage import FileSystemStorage

# Create your views here.
def login(request):
    return render(request,'administrator/login.html') #to call the page

def save(request):
    username=request.POST['username'] #to fetch the value
    password=request.POST['password']
    # logic for login
    User=auth.authenticate(username=username,password=password)
    if User is not None:
        auth.login(request,User)
        return redirect(dashboard)
    else:
        return render(request,'administrator/login.html',{'data':'invalid login'})#data to show on login screen for error
    

def dashboard(request):
    return render(request,"administrator/dashboard.html")

def upload_category(request):
    return render(request,'administrator/upload_category.html')

def save_category(request):
    category_name=request.POST['category_name']
    k=category(category=category_name)#for save data in category list
    k.save()#function to save data
    return redirect(category_list)#redirect on page


def category_list(request):
    z=category.objects.all()#show all data
    return render(request,'administrator/category_list.html',{'data':z})

def delete_category(request):
    
    x=category.objects.get(pk=request.GET['id'])#for delete id
    x.delete()
    return redirect("category_list")

def upload_product(request):
    k=category.objects.all()
    return render(request,"administrator/upload_product.html",{'data':k})

def product_upload(request):
    
    category_name=request.POST['category_name']
    product_name=request.POST['product_name']
    price=request.POST['price']
    details=request.POST['details']

    #fetch the image
    filepath = request.FILES['myfile']
    filename = filepath.name #store file name

    file_type = os.path.splitext(str(filepath))[1]

    if(file_type==".jpg" or file_type==".jpeg" or file_type==".png"):
        obj = FileSystemStorage() #creating object of FileSystemStorage Class
        k   = obj.save(filename, filepath) # using save(FileName, FilePath) function
        uploaded_file_url = obj.url(k)
        
        k1=product(product_name=product_name, category_name=category_name, price=price, details=details, image=filename)
        k1.save()
        return redirect("upload_product")
        
    else:
        return HttpResponse("Error! Invalid File")
    
def product_list(request):
    k=product.objects.all()
    return render(request, "administrator/product_list.html",{'data':k})


def delete1(request):
    x = product.objects.get(pk=request.GET['id'])
    x.delete()
    return redirect("product_list")


def logout(request):
    auth.logout(request)#for logout
    return redirect("login")


def ordertable(request):
    k=purchase.objects.all()
    return render(request, "administrator/ordertable.html",{'data':k})

def delete(request):
    x=purchase.objects.get(pk=request.GET['id'])
    x.delete()
    return redirect("ordertable")
    