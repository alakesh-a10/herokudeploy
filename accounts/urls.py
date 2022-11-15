from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
   path('home/', views.index, name='home'),
   path('register/', views.register, name='register'),
   path('login/', views.userlogin, name='login'),
   path('logout/', views.userlogout, name='logout'),
   path('', views.Products, name='products'),
   path('customer/<int:c_id>/', views.Customer, name='customer'),
   path('createOrder',views.createOrder, name='create_Order'),
   path('updateOrder/<int:o_id>/',views.updateOrder, name='update_Order'),
   path('createCust/',views.createCustomer,name='create_Customer'),
   path('updateCust/<int:c_id>/', views.updateCustomer, name='update_cust'),
   path('deleteOrder/<int:o_id>/', views.deleteOrder, name='delete_order'),
    path('user/', views.userProfile, name='userProfile'),
    
   
]


