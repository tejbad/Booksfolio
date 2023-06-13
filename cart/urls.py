from django.urls import path
from . import views
urlpatterns = [
    
   # path('buyer',views.buyer , name="buyer"),
   # path('<str:stream>/<str:branch>',views.year , name="year"),
   # path('<str:stream>/<str:branch>/<int:yr>',views.buyer_output , name="buyer_output"),
   path('add_cart/<int:id>',views.Add_cart , name="Add_cart"),
   
   path('go_to_cart',views.go_to_cart , name="go_to_cart"),

   path('remove/<int:id>',views.remove , name="remove"),
   # path('add_cart/<int:id>',views.Add_cart , name="Add_cart"),
   # path('buyer',views.buyer , name="buyer"),

   # path('ajax/load-cities/', views.load_subject, name='ajax_load_cities'),
  ]
