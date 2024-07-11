from .models import Catagory
from cart.cart import Cart

def categoryall(request):
    categoriesa = Catagory.objects.all()
    return {'categories':categoriesa}

def cart(request):
    return {'cart':Cart(request)}