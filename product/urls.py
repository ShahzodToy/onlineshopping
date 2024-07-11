from django.urls import path
from . import views

urlpatterns = [
    path('',views.product_list,name='product_list'),
    path('<slug:category_slug>/',views.product_list,name='product_list_by_category'),
    path('<int:id>/<slug:slug>/products',views.product_detail,name='product_detail'),
    path('search/', views.product_search, name='post_search'),
]