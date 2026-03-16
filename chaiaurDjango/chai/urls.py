from django.urls import path, include
from . import views

# localhost:8000/chai
# localhost:8000/chai/shop

urlpatterns = [
    path('', views.all_chai, name='all_chai'),
    path('shop/',views.shop_now,name='shop'),
    path('cart/', views.cart, name='cart'),
    path('add-to-cart/<int:chai_id>/', views.add_to_cart, name='add_to_cart'),
]