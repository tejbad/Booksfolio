from django.contrib import admin
from django.urls import path 
from . import views
from django.conf.urls import url
from django.contrib.auth import views as auth_views
urlpatterns = [
    
    path('register',views.register , name="register"),
    # path('register2',views.register2 , name="register2"),
    path('login',views.login , name='login'),
    path('logout',views.logout , name='logout'),
    path('profile_info',views.profile , name='profile'),
    path('edit_profile',views.edit_profile , name='edit_profile'),

    
    path('profile/change_password',views.change_password , name='change_password'),

    # url(r'password_reset/$', auth_views.password_reset, name='password_reset'),
    # url(r'^password_reset/done/$', auth_views.password_reset_done, name='password_reset_done'),
    # url(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$', auth_views.password_reset_confirm, name='password_reset_confirm'),
    # url(r'^reset/done/$', auth_views.password_reset_complete, name='password_reset_complete'),

  ]
