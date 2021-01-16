from django.shortcuts import render, get_object_or_404, redirect  #  renders HTML templates
from django.http import HttpResponse #  displays HttpResponse
from django.shortcuts import render

# Create your views here.
def view_cart(request):
    return render(request, "cart/cart.html")