from django.contrib import admin
from .models import Coupon

@admin.register(Coupon)
class CouponAdmin(admin.ModelAdmin):
    list_display = ['code','valid_from','valid_to','active','discount']
    list_filter = ['valid_from','valid_to','active']
    search_fields =['code']