from django.db import models
from product.models import Product
from coupons.models import Coupon
from django.core.validators import MinValueValidator,MaxValueValidator
from decimal import Decimal
from django.utils.translation import gettext_lazy as _

class Order(models.Model):
    first_name= models.CharField(_('first name'),max_length=100)
    last_name = models.CharField(_('last name'),max_length=100)
    emial = models.EmailField(_('emial'),max_length=50)
    address = models.CharField(_('address'),max_length=50)
    postal_code = models.IntegerField(_('postal code'))
    city = models.CharField(_('city'),max_length=50)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    paid = models.BooleanField(_('paid'),default=False)
    coupon = models.ForeignKey(Coupon,
                               related_name='orders',
                                null=True,blank=True,
                               on_delete=models.SET_NULL)
    discount = models.IntegerField(default=0,validators=[MinValueValidator(0),MaxValueValidator(100)])

    def __str__(self):
         return f'Order {self.id}'

    class Meta:
        ordering = ['-created']
        indexes = [
            models.Index(fields=['-created'])
        ]

    
    
    def get_total_cost_before_discount(self):
         return sum(item.get_cost() for item in self.items.all())
    
    def get_discount(self):
         total_cost = self.get_total_cost_before_discount()
         if self.discount:
              return total_cost*(self.discount/Decimal(100))
         return Decimal(0)

    def get_total_cost(self):
        total_cost = self.get_total_cost_before_discount()
        return total_cost - self.get_discount()
    
    
    
class OrderItem(models.Model):
        order = models.ForeignKey('Order',
                                  related_name='items',
                                  on_delete=models.CASCADE)
        product = models.ForeignKey(Product,
                                    related_name='order_items',
                                    on_delete=models.CASCADE)
        price = models.DecimalField(max_digits=19,
                                    decimal_places=2)
        quantity = models.PositiveIntegerField(default=1)

        def get_cost(self):
            return self.price * self.quantity


        def __str__(self):
            return self.order