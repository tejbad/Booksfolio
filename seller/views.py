from django.shortcuts import render, redirect
from .models import Seller_books 
# , Seller_nonacademic , Seller_gadgets
from django.contrib import messages
from . import models
from .forms import S_bookform

def seller_books(request):
    user = request.user
    if user.is_authenticated:
        if request.method == 'POST':
            domain = request.POST.get('domain')
            book_name = request.POST.get('book_name')
            author_name = request.POST.get('author_name')
            original_price = request.POST.get('original_price')
            demand_price = request.POST.get('demand_price')
            publish_yr = request.POST.get('publish_yr')
            yr_sem = request.POST.get('yr_sem')
            branch = request.POST.get('branch')
            book_img = request.FILES['book_img']
            # print(demand_price)
    # Have to change ---->>>>>>
            demand_price = int(demand_price)
            if demand_price <= 200:
                shown_price = int(demand_price) + 15
            elif 200 <= demand_price <= 500:
                shown_price = int(demand_price) + 25
            elif 500 <= demand_price <= 1000:
                shown_price = int(demand_price) + 35
            elif 1000 <= demand_price :
                shown_price = int(demand_price) + 50
            # print(demand_price)


    # ----------------
            sb = Seller_books.objects.create(user_id=user.id, product_type= "academic" , book_name=book_name,author_name=author_name,original_price=original_price,demand_price=demand_price,publish_yr=publish_yr,yr_sem=yr_sem,branch=branch,book_img=book_img, shown_price =shown_price , domain = domain)
            sb.save()
            return redirect('seller_books')
        else:
            user_books = Seller_books.objects.filter(user_id = user)
            return render(request, 'seller_in.html' , {'user_books':user_books} )
    else:
        messages.error(request,'Please Login first')
        return redirect('login')        


def seller_nonacademic(request):
    user = request.user
    if user.is_authenticated:
        if request.method == 'POST':
            # domain = request.POST.get('domain')
            book_name = request.POST.get('book_name')
            author_name = request.POST.get('author_name')
            original_price = request.POST.get('original_price')
            demand_price = request.POST.get('demand_price')
            publish_yr = request.POST.get('publish_yr')
            disc = request.POST.get('disc')
            # branch = request.POST.get('branch')
            book_img = request.FILES['book_img']

    # Have to change ---->>>>>>
            demand_price = int(demand_price)
            if demand_price <= 200:
                shown_price = int(demand_price) + 15
            elif 200 <= demand_price <= 500:
                shown_price = int(demand_price) + 25
            elif 500 <= demand_price <= 1000:
                shown_price = int(demand_price) + 35
            elif 1000 <= demand_price :
                shown_price = int(demand_price) + 50
            # print(demand_price)
    # ----------------
            sb = Seller_books.objects.create(user_id=user.id, product_type= "non_academic" , book_name=book_name,author_name=author_name,original_price=original_price,demand_price=demand_price,publish_yr=publish_yr,disc=disc,book_img=book_img, shown_price =shown_price )
            sb.save()
            return redirect('seller_books')
        else:
            user_books = Seller_books.objects.filter(user_id = user)
            return render(request, 'seller_in.html' , {'user_books':user_books} )
    else:
        messages.error(request,'Please Login first')
        return redirect('login')


def seller_gadgets(request):
    user = request.user
    if user.is_authenticated:
        if request.method == 'POST':
            # domain = request.POST.get('domain')
            gadget_name = request.POST.get('gadget_name')
            manufacturer = request.POST.get('manufacturer')
            manufacturer_yr = request.POST.get('manufacturer_yr')

            original_price = request.POST.get('original_price')
            demand_price = request.POST.get('demand_price')
            # publish_yr = request.POST.get('publish_yr')
            disc = request.POST.get('disc')
            # branch = request.POST.get('branch')
            gadget_img = request.FILES['gadget_img']

    # Have to change ---->>>>>>
            demand_price = int(demand_price)
            if demand_price <= 200:
                shown_price = int(demand_price) + 15
            elif 200 <= demand_price <= 500:
                shown_price = int(demand_price) + 25
            elif 500 <= demand_price <= 1000:
                shown_price = int(demand_price) + 35
            elif 1000 <= demand_price :
                shown_price = int(demand_price) + 50
            # print(demand_price)
    # ----------------
            sb = Seller_books.objects.create(user_id=user.id, product_type="gadget" ,book_name=gadget_name,manufacturer=manufacturer,original_price=original_price,demand_price=demand_price,manufacturer_yr=manufacturer_yr,disc=disc,book_img=gadget_img, shown_price =shown_price )
            sb.save()
            return redirect('seller_books')
        else:
            user_books = Seller_books.objects.filter(user_id = user)
            return render(request, 'seller_in.html' , {'user_books':user_books} )
    else:
        messages.error(request,'Please Login first')
        return redirect('login')        
    
# def s_edit(request, id):
#     # request.user is Seller_books.owner :
#     if Seller_books.objects.filter(id=id).exists():
#         user = request.user
#         obj = Seller_books.objects.get(id=id)
    
#         if obj in Seller_books.objects.filter(user_id = user):
#             print("inside delete")
#             form = S_bookform(request.POST, request.FILES ,instance=obj)
#             if request.method == 'POST':
#                 if request.POST['submit'] == 'delete':
#                     if 1:
#                     # Seller_books.objects.filter(user_id = user and id=id) :     
#                         print("Valid obj")
#                         Seller_books.objects.filter(id=id).delete()
#                         return redirect('s_edit')
#                     else:
#                         print("Valid obj")
#                 if form.is_valid():
#                     form.save()
#             return render(request, 'seller_edit.html',{'form': form,'obj':obj})
#         else:
#             print("object does not exist")
#             return redirect('seller_books')
#     else:
#         return redirect('seller_books')
    
def book_del(request , id):
    user = request.user
    # print(user)
    # print(id)
    if Seller_books.objects.filter(user_id=user.id , id = id).exists():
        # print("hi   ")
        Seller_books.objects.filter(id=id).delete()
    else:
        return redirect("seller_books")        
    return redirect("seller_books")
