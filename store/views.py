from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Product

class ProductListView(ListView):
    """商品列表視圖"""
    model = Product
    template_name = 'store/product_list.html'
    context_object_name = 'products'
    paginate_by = 12  # 每頁顯示12個商品

class ProductDetailView(DetailView):
    """商品詳情視圖"""
    model = Product
    template_name = 'store/product_detail.html'
    context_object_name = 'product' 