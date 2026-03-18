from django.contrib import admin
from .models import chaiVarity , availableTea, Cart ,cartItem, Review

# Register your models here.
admin.site.register(chaiVarity)
admin.site.register(availableTea)
admin.site.register(Cart)
admin.site.register(cartItem)
admin.site.register(Review)
