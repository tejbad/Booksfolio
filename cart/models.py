from django.db import models
# from django.contrib.auth.models import User
from accounts.models import User

from seller.models import Seller_books
# ,Seller_gadgets, Seller_nonacademic
# Create your models here.
class Cart(models.Model):
    usr = models.ForeignKey(User,to_field='id',on_delete=models.SET_NULL,related_name='cart_owner',null= True)
    item = models.ManyToManyField(Seller_books ,related_name='cart_items' , blank = True)
    # nonac_item = models.ManyToManyField(Seller_nonacademic ,related_name='cart_items_non_academic')
    # gad_item = models.ManyToManyField(Seller_gadgets ,related_name='cart_items_gad' , blank= True)

    total = models.IntegerField(default=00)

    def get_cart_total(self):
        return sum([Cart.item.demand_price for Cart in self.item.all()])


class Order(models.Model):
    user = models.ForeignKey(User,to_field='id',on_delete=models.SET_NULL,related_name='oder_owner',null= True)
    order_item = models.ManyToManyField(Seller_books)
    # order_nonac = models.ManyToManyField(Seller_nonacademic)
    # order_gad = models.ManyToManyField(Seller_gadgets)

    date_ordered = models.DateTimeField(auto_now=True)
    address = models.TextField(blank=True, default="" ,)
    primary_mob = models.CharField(default="" , max_length = 12)
    secondary_mob = models.CharField(default="" , max_length = 12)
    total_price = models.IntegerField(default=00)

    def get_cart_total(self):
        return sum([Cart.item.demand_price for Cart in self.item.all()])