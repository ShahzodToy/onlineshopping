from django.contrib import admin
from .models import Product,Catagory,Review
@admin.register(Catagory)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name','slug']
    prepopulated_fields = {'slug':('name',)}

admin.site.register(Review)

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name','category','price','created','available']
    list_editable = ['price','available']
    prepopulated_fields = {'slug':('name',)}
    list_filter = ['created','category','available']