from django.shortcuts import render
from django.views import View
from .models import *
class ProductView(View):
 def get(self,request):
  topwears = Product.objects.filter(category='TW')  
  mobile = Product.objects.filter(category='M')  
  bottom = Product.objects.filter(category='BW')  
  laptop = Product.objects.filter(category='L') 
  return render(request, 'app/home.html',{'topwears': topwears,
    'bottom': bottom,'laptop':laptop,'mobile':mobile}) 

def home(request):
 return render(request, 'app/home.html')

class ProductDetailView(View):
 def get(self , request, pk):
  product = Product.objects.get(pk=pk)
  return render(request, 'app/productdetail.html', {'product':product})

def add_to_cart(request):
 return render(request, 'app/addtocart.html')

def buy_now(request):
 return render(request, 'app/buynow.html')

def profile(request):
 return render(request, 'app/profile.html')

def address(request):
 return render(request, 'app/address.html')

def orders(request):
 return render(request, 'app/orders.html')

def change_password(request):
 return render(request, 'app/changepassword.html')

def mobile(request, data=None):
  if data == None:
    mobiles = Product.objects.filter(category='M')
  elif data == 'below': 
    mobiles = Product.objects.filter(category='M').filter(discounted_price__lt = 20000)
  elif data == 'above': 
    mobiles = Product.objects.filter(category='M').filter(discounted_price__gt = 20000)
  else : 
    mobiles = Product.objects.filter(category='M').filter(brand=data)
  return render(request, 'app/mobile.html',{'mobiles' : mobiles})

def laptop(request, data = None):
  if data == None:
    laptop = Product.objects.filter(category = 'L')
  elif data == 'below': 
    laptop = Product.objects.filter(category='L').filter(discounted_price__lt=50000)
  elif data == 'above': 
    laptop = Product.objects.filter(category='L').filter(discounted_price__lt=50000)
  else : 
    laptop = Product.objects.filter(category='L').filter(brand=data)
  return render(request,'app/laptop.html',{'laptop':laptop})

def topwear(request,data=None):
  if data==None:
   topwear = Product.objects.filter(category='TW')
  else :
   topwear = Product.objects.filter(category='TW').filter(brand = data)
  return render(request,'app/topwear.html',{'topwear':topwear})

def bottomwear(request,data= None):
  if data == None:
    bottomwear = Product.objects.filter(category = 'BW')
  else :
    bottomwear = Product.objects.filter(category='BW').filter(brand= data)
  return render(request,'app/bottomwear.html',{'bottomwear':bottomwear})

def login(request):
 return render(request, 'app/login.html')

def customerregistration(request):
 return render(request, 'app/customerregistration.html')

def checkout(request):
 return render(request, 'app/checkout.html')
