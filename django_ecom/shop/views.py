from django.shortcuts import render
from django.http import HttpResponse
from .models import Product
from math import ceil

def index(request):
    products = Product.objects.all()
    n = len(products)
    n_slides = ceil(n / 4)
    # Chunk products into sublists of 4 items each
    allProds = [products[i:i+4] for i in range(0, n, 4)]
    params = {'allProds': allProds, 'slide_range': range(n_slides), 'nSlides': n_slides}
    return render(request, 'shop/index.html', params)

def about(request):
    return render(request,'shop/about.html')

def contact(request):
    return HttpResponse("Contact Me")

def tracker(request):
    return HttpResponse("Tracker")

def prodview(request):
    return HttpResponse("Product View")

def search(request):
    return HttpResponse("Search")

def chkout(request):
    return HttpResponse("Check Out")