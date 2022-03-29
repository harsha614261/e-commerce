from django.contrib import admin
from django.urls import path
from .import views
urlpatterns = [
    path('',views.home,name='home'),
    path('login',views.login,name='login'),
    path('register',views.register,name='register'),
    path('product',views.product,name='product'),
    path('account',views.account,name='account'),
    path('GetDetails/<slug>',views.GetDetails,name='GetDetails'),
    path('BuyNow/<slug>',views.BuyNow,name='BuyNow'),
    path('AddToCart/<slug>',views.AddToCart,name='AddToCart'),
    #path('BuyNow/<s>',views.success,name="success"),
    path('logout',views.logout,name='logout'),
    path('order',views.order,name='order'),
    path('cart',views.Mycart,name='cart'),
    path('SendQuery',views.SendQuery,name="SendQuery"),
    path('owner',views.owner,name="owner"),
    ]