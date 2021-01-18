from django.shortcuts import render, get_object_or_404, redirect  #  renders HTML templates
from django.http import HttpResponse #  displays HttpResponse
from django.shortcuts import render
from products.models import Product

# Create your views here.
def view_cart(request):
    return render(request, "cart/cart.html")


def add_to_cart(request, item_id):

    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    cart = request.session.get('cart', {})

    if item_id in list(cart.keys()):
        cart[item_id] += quantity
    else:
        cart[item_id] = quantity

    request.session['cart'] = cart
    return redirect(redirect_url)
