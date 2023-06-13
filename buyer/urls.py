from django.urls import path
from . import views
urlpatterns = [
    
   path('buyer/<int:pg>',views.buyer , name="buyer"),
   path('buyer_nonacademic/<int:pg>',views.buyer_nonacademic , name="buyer"),
   path('buyer_gadgets/<int:pg>',views.buyer_gadgets , name="buyer"),
   path('search_buyer/<int:pg>',views.search_buyer , name="buyer"),
   path('buy_static_page/<int:pg>/<str:course>',views.buy_static_page , name="buy_static_page"),
   path('buy_static_with_type/<int:pg>/<str:p_type>',views.buy_static_with_type , name="buy_static_with_type"),
   path('solo_product/<int:id>',views.solo_product , name="solo_product"),

# solo_product

   
   # path('<str:stream>/<str:branch>',views.year , name="year"),
   # path('<str:stream>/<str:branch>/<int:yr>',views.buyer_output , name="buyer_output"),
   # path('<str:stream>',views.branch , name="branch"),
   path('place_order',views.place_order , name="place_order"),
   path('checkout',views.checkout , name="checkout"),

   # path('ajax/load-cities/', views.load_subject, name='ajax_load_cities'),
  ]
