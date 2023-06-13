from django.shortcuts import render ,redirect
from seller.models import Seller_books
from .forms import Buyer_booksForm
from cart.models import  Cart ,Order
from django.contrib.auth.decorators import login_required


def buy_static_page(request , pg ,course):
    rng = (pg*9)
    buy_books = Seller_books.objects.filter(product_type = "academic", is_ordered = False  , domain = course)[:rng]
    # print(buy_books)
    return render(request, 'buyer.html' ,{ 'buy_books': buy_books , 'pg' : pg})

def buy_static_with_type(request , pg ,p_type):
    rng = (pg*9)
    buy_books = Seller_books.objects.filter(product_type = p_type , is_ordered = False  )[:rng]
    # print(buy_books)
    return render(request, 'buyer.html' ,{ 'buy_books': buy_books , 'pg' : pg})


def search_buyer(request , pg):
    user = request.user
    rng = (pg*9)
    if request.method == 'POST':
        search = request.POST.get('search')
        # print(search , " t")
        if search:
            buy_books = Seller_books.objects.filter(product_type = "academic", is_ordered = False  , book_name__icontains=search)[:rng]
            
            # print(buy_books)
            return render(request, 'buyer.html' ,{ 'buy_books': buy_books , 'pg' : pg})
        # else:
    return render(request, 'buyer.html' ,{ 'pg' : pg})

def buyer(request , pg):
    user = request.user
    rng = (pg*9)
    if request.method == 'POST':
        branch = request.POST.get('branch')
        yr_sem = request.POST.get('yr_sem')
        book_name = request.POST.get('book_name')
        domain = request.POST.get('domain')

        if book_name == "All":
            buy_books = Seller_books.objects.filter(branch = branch , yr_sem = yr_sem , is_ordered = False , domain = domain).order_by('shown_price')[:rng]
        else :
            buy_books = Seller_books.objects.filter(branch = branch , yr_sem = yr_sem , book_name = book_name ,is_ordered = False , domain = domain)[:rng]
        # print(buy_books)

        return render(request, 'buyer.html' ,{ 'buy_books': buy_books , 'pg' : pg})
    return render(request, 'buyer.html' ,{ 'pg' : pg})

def buyer_nonacademic(request , pg):
    user = request.user
    rng = (pg*9)
    if request.method == 'POST':
        search = request.POST.get('search')
        if search :
            buy_books = Seller_books.objects.filter(product_type = "non_academic", is_ordered = False  , book_name__icontains=search)[:rng]
            # print(buy_books)
            return render(request, 'buyer.html' ,{ 'buy_books': buy_books , 'pg' : pg})

    return render(request, 'buyer.html' ,{ 'pg' : pg})


def buyer_gadgets(request , pg):
    user = request.user
    rng = (pg*9)
    if request.method == 'POST':
        search = request.POST.get('search')
        if search :
            buy_books = Seller_books.objects.filter(product_type = "gadget" , is_ordered = False , book_name__icontains=search)[:rng]
            # print(buy_books)
            return render(request, 'buyer.html' ,{ 'buy_books': buy_books , 'pg' : pg})

    return render(request, 'buyer.html' ,{ 'pg' : pg})    

@login_required(login_url="/accounts/login")
def checkout(request):
    user = request.user
    # if 
    checkout_items = Cart.objects.filter(usr_id = user.id) 
    for obj in checkout_items:
        checkout_items = obj.item.all()
    total = 0
    for i in checkout_items:
        total = total + i.shown_price
    return render(request, 'cart.html',{'checkout_items' : checkout_items , 'total' : total })

@login_required(login_url="/accounts/login")
def place_order(request):
    user = request.user
    if request.method == 'POST':
        address = request.POST.get('address')
        primary_mob = request.POST.get('primary_mob')
        secondary_mob = request.POST.get('secondary_mob')

        order_books = Cart.objects.filter(usr = user)
        # print(order_books)

        for obj in order_books:
            order_books = obj.item.all()
        total = 0 
        for i in order_books:
            i.is_ordered = True
            total = total + i.shown_price
            i.save()
        # print(total)
        ord = Order.objects.create(user_id = user.id ,  address = address , primary_mob = primary_mob , secondary_mob = secondary_mob , total_price = total)
        ord.order_item.set(order_books)
        ord.save()
        Cart.objects.filter(usr = user).delete()
        return redirect('/')


def solo_product(request , id):
    solo_p = Seller_books.objects.get(id = id)
    return render(request, 'new.html' ,{ 'solo_p': solo_p })