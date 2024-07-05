from django.shortcuts import render, get_object_or_404
from core.models import Products, Pro_images
from django.db.models import Q


def index(request):
    pros = Products.objects.filter(is_avail=True)
    return render(request, 'core/index.html',{'pros':pros})

def about(request):
    return render(request, 'core/about.html')

def products(request):
    pros = Products.objects.filter(is_avail=True)
    return render(request, 'core/products.html',{'pros':pros})

def product(request, pro_id):
    pro = get_object_or_404(Products, id=pro_id)
    imgs = Pro_images.objects.filter(product=pro_id)
    pros = Products.objects.filter(Q(is_avail=True) & Q(is_featured=True))
    return render(request, 'core/product.html',{'pro':pro,'imgs':imgs,'pros':pros})

def gallery(request):
    return render(request, 'core/gallery.html')

def contact(request):
    return render(request, 'core/contact.html')