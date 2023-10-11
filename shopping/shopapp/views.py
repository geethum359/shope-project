
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm 
from . forms import CustomUserCreationForm
from . models import Products,category,Cart,CartItem
from django.contrib.auth import authenticate,login,logout,forms
from django.http import HttpResponse
from django.views import View
from django.contrib.auth.models import User

def home(request):
    p = {
        'pro': Products.objects.all()
    }
    return render(request, 'home.html', p)
    

class categoryView(View):
    def get(self,request,val):
        products=Products.objects.filter(category=val)
        pro_name= Products.objects.filter(category=val).values('pro_name')
        return render(request,'category.html',locals())
    
class productDetails(View):
    def get(self,request,pk):
        products=Products.objects.get(pk=pk)
        return render(request,'product_details.html',locals())


def add_to_cart(request, product_id):
 if request.user.is_authenticated:
    product = Products.objects.get(pk=product_id)
    cart, created = Cart.objects.get_or_create()
    cart_item, created = CartItem.objects.get_or_create(cart=cart, product=product)
    if not created:
        cart_item.quantity += 1
        cart_item.save()
    return redirect('cart')
 else:
     return redirect('signup')

def cart(request):
    cart, created = Cart.objects.get_or_create()
    cart_items = CartItem.objects.filter(cart=cart)
    total_price = sum(item.product.pro_price * item.quantity for item in cart_items)
    return render(request, 'cart.html', {'cart_items': cart_items, 'total_price': total_price})



# ---------------------------------login , signup and logout -----------------------------------------

def signup(request):
    form=CustomUserCreationForm()
    if(request.method=='POST'):
        form=CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    return render(request,'signup.html',{"form":form})

def login(request):
    if request.user.is_authenticated:
        return render(request,'home.html')
    else:
        if(request.method=='POST'):
            name=request.POST.get('username')
            password=request.POST['p']
            user=authenticate(username=name,password=password)
            if user:
                login(request,user)
                return redirect('home')
            else:
                return HttpResponse('Invalid .......... NO user found !')
        return render(request,'login.html')


def user_logout(request):
    logout(request)
    return redirect('login')