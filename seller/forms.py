from django import forms
from .models import  Seller_books
from django.forms import ModelForm
from .models import  books
# CHOICES= books.objects.all()

author_ch = [ ('nirali','nirali'),('abcd','abcd')]
ch= [ ('0','99'),('5456','45')]

class S_bookform(ModelForm):
   
   book_name = forms.CharField(max_length=50)
   author_name = forms.ChoiceField(choices=author_ch)
#    choice_(author_name)
   original_price = forms.CharField()
   demand_price = forms.IntegerField()
   publish_yr = forms.ChoiceField(choices=ch)
   book_img = forms.ImageField(required=True)

   class Meta:
      model = Seller_books
      fields = ['book_name', 'author_name', 'original_price','demand_price', 'publish_yr','book_img']
         # book_name = forms.ChoiceField(choices=CHOICES)
         # Select(choices=CHOICES)
        # widgets = {
        #     'book_name': class:            
        #     }

   
