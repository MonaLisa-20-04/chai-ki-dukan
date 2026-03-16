from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.

class chaiVarity(models.Model):
    CHAI_TYPE_CHOICE = [
        ('ML' , 'MASALA CHAI'),
        ('GR' , 'GINGER CHAI'),
        ('KI' , 'KIWI CHAI'),
        ('PL' , 'PLAIN CHAI'),
        ('EL' , 'ELAICHI CHAI'),
    ]
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='chais/')
    date_added = models.DateTimeField(default=timezone.now)
    type = models.CharField(max_length=2 , choices=CHAI_TYPE_CHOICE)
    description = models.TextField(default='')
    price = models.DecimalField(max_digits=6, decimal_places=2, default='0.00')

    def __str__(self):
        return self.name
    
class availableTea(models.Model):
    CHAI_TYPE_CHOICE = [
        ('ML' , 'MASALA CHAI'),
        ('GR' , 'GINGER CHAI'),
        ('KI' , 'KIWI CHAI'),
        ('PL' , 'PLAIN CHAI'),
        ('EL' , 'ELAICHI CHAI'),
    ]
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='chais/')
    date_added = models.DateTimeField(default=timezone.now)
    type = models.CharField(max_length=2 , choices=CHAI_TYPE_CHOICE)
    description = models.TextField(default='')
    price = models.DecimalField(max_digits=6, decimal_places=2, default='0.00')

    def __str__(self):
        return self.name

class Cart(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.user.username}'s cart"
    
    def total_price(self):
        return sum(item.subtotal() for item in self.cartitem_set.all())
    
class cartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    chai = models.ForeignKey(availableTea, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.quantity} * {self.chai.name}"
    
    def subtotal(self):
        return self.chai.price * self.quantity