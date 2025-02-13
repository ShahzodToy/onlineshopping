from django.shortcuts import render
from .models import Order,OrderItem
from .forms import OrderCreateForm
from cart.cart import Cart


def order_create(request):
    cart = Cart(request)
    if request.method == 'POST':
        form  = OrderCreateForm(request.POST)
        if form.is_valid():
            order= form.save(commit=False)
            if cart.coupon:
                order.coupon = cart.coupon
                order.discoun = cart.coupon.discount
            order.save()
            for item in cart:
                OrderItem.objects.create(
                    order=order,
                    product = item['product'],
                    price  =item['price'],
                    quantity = item['quantity']
                )
            cart.clear()
            return render(request,'created.html',{'order':order})
    else: 
        form =  OrderCreateForm()
    return render(request,'checkout.html',{'cart':cart,'form':form})
