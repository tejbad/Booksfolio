from django.urls import path
from . import views
urlpatterns = [
  # path('s_edit/<int:id>',views.s_edit , name="edit"),
  path('seller',views.seller_books , name="seller_books"),
  
  path('seller_nonacademic',views.seller_nonacademic , name="seller_nonacademic"),
  
  path('seller_gadgets',views.seller_gadgets , name="seller_gadgets"),

  path('seller/delete/<int:id>',views.book_del , name="book_del")
  ] 

