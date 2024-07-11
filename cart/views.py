from django.shortcuts import render,get_object_or_404,redirect
from django.views.decorators.http import require_POST
from product.models import Product,Catagory
from .cart import Cart
from .forms import CartAddForm

from coupons.forms import CouponAppllyForm

@require_POST
def cart_add(request,product_id):
    cart = Cart(request)
    product = get_object_or_404(Product,id=product_id)
    form = CartAddForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        cart.add(product=product,
                 quantity = cd['quantity'],
                 override_quantity=cd['override'])
    return redirect('cart_detail')
@require_POST
def remove(request,product_id):
    cart = Cart(request)
    product = get_object_or_404(Product,id = product_id)
    cart.remove(product)
    return redirect('cart_detail')

def cart_detail(request):
    cart = Cart(request)
    cart_add_form  = CartAddForm()
    coupon_apply_form = CouponAppllyForm()
    return render(request,'cart.html',{'cart':cart,'coupon_apply_form':coupon_apply_form,'cart_add_form':cart_add_form})