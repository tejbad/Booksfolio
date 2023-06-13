from django.db import models
from accounts.models import User

# from django.contrib.auth.models import User
# Create your models here.
from django.dispatch import receiver
import os

class books(models.Model):
    book = models.CharField(max_length=100 ,default="",blank=False)


class Seller_books(models.Model):
    user = models.ForeignKey(User,to_field='id',on_delete=models.CASCADE,related_name='s_books')
    
    product_type = models.CharField(max_length=100 ,default="",blank=False)
    domain = models.CharField(max_length=100 ,default="",blank=True)
    book_name = models.CharField(max_length=100 ,default="",blank=False)
    author_name = models.CharField(max_length=100, default="",blank=True)
    original_price = models.IntegerField(default=00,blank=False)
    demand_price = models.IntegerField(default=00,blank=False)
    publish_yr = models.CharField(max_length=100, default="",blank=True)
    # IntegerField(default=00,blank=True)
    book_img = models.ImageField(upload_to='Book_img',blank=True,default="")
    is_ordered = models.BooleanField(default=False)
    shown_price = models.IntegerField(default=00,blank=False)
    yr_sem = models.CharField(max_length=100 ,default="",blank=True)
    branch = models.CharField(max_length=100 ,default="",blank=True)
    disc = models.CharField(max_length=100 ,default="",blank=True)
    manufacturer = models.CharField(max_length=100 ,default="",blank=True)
    manufacturer_yr = models.IntegerField(default=00,blank=True)
    def owner(self):
        return self.user

    class Meta:
        db_table = 's_books'    
@receiver(models.signals.post_delete, sender=Seller_books)
def auto_delete_file_on_delete(sender, instance, **kwargs):
    """
    Deletes file from filesystem
    when corresponding `MediaFile` object is deleted.
    """
    if instance.book_img:
        if os.path.isfile(instance.book_img.path):
            os.remove(instance.book_img.path)

@receiver(models.signals.pre_save, sender=Seller_books)
def auto_delete_file_on_change(sender, instance, **kwargs):
    """
    Deletes old file from filesystem
    when corresponding `MediaFile` object is updated
    with new file.
    """
    if not instance.pk:
        return False

    try:
        old_file = sender.objects.get(pk=instance.pk).book_img
    except sender.DoesNotExist:
        return False

    new_file = instance.book_img
    if not old_file == new_file:
        if os.path.isfile(old_file.path):
            os.remove(old_file.path)


# class Seller_nonacademic(models.Model):
#     user = models.ForeignKey(User,to_field='id',on_delete=models.CASCADE,related_name='s_nonacademic')
    
#     # domain = models.CharField(max_length=100 ,default="",blank=False)
#     book_name = models.CharField(max_length=100 ,default="",blank=False)
#     disc = models.CharField(max_length=100 ,default="",blank=False)
#     author_name = models.CharField(max_length=100, default="",blank=False)
#     original_price = models.IntegerField(default=00,blank=False)
#     demand_price = models.IntegerField(default=00,blank=False)
#     publish_yr = models.IntegerField(default=00,blank=False)
#     # DateField(default=0000-00-00)
    
#     # bargain = models.BooleanField(default=False)
#     book_img = models.ImageField(upload_to='Book_nonacademic',blank=True,default="")
#     is_ordered = models.BooleanField(default=False)
#     shown_price = models.IntegerField(default=00,blank=False)
#     # stream = models.CharField(max_length=100 ,default="",blank=True)
#     # yr_sem = models.CharField(max_length=100 ,default="",blank=False)
#     # IntegerField(default=00)
    
#     def owner(self):
#         return self.user

#     class Meta:
#         db_table = 's_nonacademic'    
# @receiver(models.signals.post_delete, sender=Seller_nonacademic)
# def auto_delete_file_on_delete(sender, instance, **kwargs):
#     """
#     Deletes file from filesystem
#     when corresponding `MediaFile` object is deleted.
#     """
#     if instance.book_img:
#         if os.path.isfile(instance.book_img.path):
#             os.remove(instance.book_img.path)

# @receiver(models.signals.pre_save, sender=Seller_nonacademic)
# def auto_delete_file_on_change(sender, instance, **kwargs):
#     """
#     Deletes old file from filesystem
#     when corresponding `MediaFile` object is updated
#     with new file.
#     """
#     if not instance.pk:
#         return False

#     try:
#         old_file = sender.objects.get(pk=instance.pk).book_img
#     except sender.DoesNotExist:
#         return False

#     new_file = instance.book_img
#     if not old_file == new_file:
#         if os.path.isfile(old_file.path):
#             os.remove(old_file.path)


# class Seller_gadgets(models.Model):
#     user = models.ForeignKey(User,to_field='id',on_delete=models.CASCADE,related_name='s_gadgets')
    
#     # domain = models.CharField(max_length=100 ,default="",blank=False)
#     gadget_name = models.CharField(max_length=100 ,default="",blank=False)
#     disc = models.CharField(max_length=100 ,default="",blank=False)
#     manufacturer = models.CharField(max_length=100, default="",blank=False)
#     original_price = models.IntegerField(default=00,blank=False)
#     demand_price = models.IntegerField(default=00,blank=False)
#     manufacturer_yr = models.IntegerField(default=00,blank=False)
#     # DateField(default=0000-00-00)
    
#     # bargain = models.BooleanField(default=False)
#     gadget_img = models.ImageField(upload_to='gadgets',blank=True,default="")
#     is_ordered = models.BooleanField(default=False)
#     shown_price = models.IntegerField(default=00,blank=False)
#     # stream = models.CharField(max_length=100 ,default="",blank=True)
#     # yr_sem = models.CharField(max_length=100 ,default="",blank=False)
#     # IntegerField(default=00)
    
#     def owner(self):
#         return self.user

#     class Meta:
#         db_table = 's_gadgets'    
# @receiver(models.signals.post_delete, sender=Seller_gadgets)
# def auto_delete_file_on_delete(sender, instance, **kwargs):
#     """
#     Deletes file from filesystem
#     when corresponding `MediaFile` object is deleted.
#     """
#     if instance.gadget_img:
#         if os.path.isfile(instance.gadget_img.path):
#             os.remove(instance.gadget_img.path)

# @receiver(models.signals.pre_save, sender=Seller_gadgets)
# def auto_delete_file_on_change(sender, instance, **kwargs):
#     """
#     Deletes old file from filesystem
#     when corresponding `MediaFile` object is updated
#     with new file.
#     """
#     if not instance.pk:
#         return False

#     try:
#         old_file = sender.objects.get(pk=instance.pk).gadget_img
#     except sender.DoesNotExist:
#         return False

#     new_file = instance.gadget_img
#     if not old_file == new_file:
#         if os.path.isfile(old_file.path):
#             os.remove(old_file.path)