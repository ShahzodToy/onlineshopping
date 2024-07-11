from django.shortcuts import render,redirect
from django.views.decorators.http import require_POST
from cart.cart import Cart
from .forms import CouponAppllyForm
from .models import Coupon
from django.utils import timezone

@require_POST
def coupon_apply(request):
    now = timezone.now()
    form = CouponAppllyForm(request.POST)
    if form.is_valid():
        code = form.cleaned_data['code']
        try:
            coupon = Coupon.objects.get(code__iexact=code,
                                        valid_from__lte=now,
                                        valid_to__gte=now,
                                        active=True)
            request.session['coupon_id'] = coupon.id
        except Coupon.DoesNotExist:
            request.session['coupon_id'] = None
    return redirect('cart_detail')
