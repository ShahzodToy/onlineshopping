from django.contrib import admin
from .models import OrderItem,Order


class OrderItemInlines(admin.TabularInline):
    model = OrderItem
    raw_id_fields = ['product']

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['id','first_name','last_name','emial','address','postal_code','city','paid','coupon']
    list_filter = ['created','updated','paid']
    inlines =[OrderItemInlines]
    