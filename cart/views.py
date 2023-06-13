from django.shortcuts import render
from django.shortcuts import render ,redirect
from seller.models import Seller_books
from .models import Cart
from django.contrib import messages
# Create your views here.
from django.contrib.auth.decorators import login_required

@login_required(login_url="/accounts/login")
def go_to_cart(request ):
    user = request.user
    cart_items = Cart.objects.filter(usr=user)    
    # function for adding all book's price ---->>>>
    total = 0
    for ob in cart_items:
        cart_items =  ob.item.all()
    total = 0
    for i in cart_items:
        total = total + i.shown_price
    # if 
    # crt_obj = Cart.objects.get(usr = user)
    # print(cart_items)
    return render(request, 'cart.html', {'cart_items' : cart_items , 'total':total})

@login_required(login_url="/accounts/login")
def remove(request , id):
    usr = request.user
    crt = Cart.objects.get(usr_id=usr.id )
    itm = Seller_books.objects.get(id=id)
    crt.item.remove(itm)
    return redirect("go_to_cart")

@login_required(login_url="/accounts/login")
def Add_cart(request , id):
    user = request.user
    if Cart.objects.filter(usr = user , item = id).exists():
        messages.error(request,'Item already exist')
        items =  Cart.objects.filter(usr =user)
        return redirect(go_to_cart)        
    else:
        if Cart.objects.filter(usr =user).exists():
            crt = Cart.objects.get(usr=user )
        else:
            crt = Cart.objects.create(usr=user )
        itm = Seller_books.objects.get(id=id)
        crt.item.add(itm)
        cart_items = Cart.objects.filter(usr=user)
        return redirect(go_to_cart)        
