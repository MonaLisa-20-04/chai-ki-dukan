from django.shortcuts import render
from .models import chaiVarity, availableTea, Cart, cartItem
from django.shortcuts import get_object_or_404 , redirect
from django.contrib.auth.decorators import login_required

# Create your views here.


def all_chai(request):
    tea = chaiVarity.objects.all()
    return render(request, 'chai/all_chai.html' , {
        'chais' : tea , 
        'hero_image' : '/media/chais/hero_img.jpg'
    })

def shop_now(request):
    chai = availableTea.objects.all()
    return render(request, 'chai/shop.html' , {'chais' : chai})

@login_required
def add_to_cart(request, chai_id):
    chai = get_object_or_404(availableTea, id=chai_id)
    cart, created = Cart.objects.get_or_create(user=request.user)
    cart_item, item_created = cartItem.objects.get_or_create(cart=cart , chai=chai)
    if not item_created:
        cart_item.quantity += 1
        cart_item.save()
    return redirect('cart')

@login_required
def cart(request):
    cart, created = Cart.objects.get_or_create(user=request.user)
    items = cart.cartitem_set.all()
    return render(request, 'chai/cart.html',{
        'cart': cart,
        'items': items
    })