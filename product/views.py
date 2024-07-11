from django.shortcuts import render,get_object_or_404,redirect
from .models import Product,Catagory,Review
from cart.forms import CartAddForm
from django.views.decorators.http import require_POST
from django.db.models import Count
from .forms import ReviewForm,SearchForm
from django.contrib.postgres.search import SearchVector


def product_list(request,category_slug=None):
    category = None
    products1  = Product.objects.filter(available = True)
    products = products1.annotate(total_review = Count('product_review'))
    categories = Catagory.objects.annotate(total_number = Count('products'))
    recent_products = products.order_by('-created')[:12]
    
    if category_slug:
        category = get_object_or_404(Catagory,slug=category_slug)
        products = products.filter(category=category)
    return render(request,'index.html',{'products':products,'category':category,'categories':categories,'recent_products':recent_products,'category_slug':category_slug,'products1':products1})

def product_detail(request,slug,id):
    product_qr = Product.objects.annotate(total_review = Count('product_review'))
    product = get_object_or_404(product_qr,slug=slug,id=id)
    cart_add_form  = CartAddForm()
    reviews = Review.objects.filter(product=product)
    if request.method =='POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            
            cd = form.cleaned_data
            Review.objects.create(
                name = cd['name'],
                review = cd['review'],
                emial = cd['emial'],
                product = product
            )
            
            return redirect('product_detail',slug =product.slug,id = product.id)
    else:
        form = ReviewForm()
    return render(request,'detail.html',{'product':product,'cart_add_form':cart_add_form,'form':form,'reviews':reviews})

def product_search(request):
    form = SearchForm()
    query = None
    results = []
    if 'query' in request.GET:
        form = SearchForm(request.GET)
        if form.is_valid():
            query = form.cleaned_data['query']
            results = Product.objects.annotate(
                search=SearchVector('title', 'content'),).filter(search=query)
    return render(request,
                  'search.html',
                  {'form': form,
                   'query': query,
                   'results': results})

