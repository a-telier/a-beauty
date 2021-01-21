from django.shortcuts import render, redirect, reverse  #  renders HTML templates
from django.http import HttpResponse #  displays HttpResponse
from django.contrib import messages
from products.models import Product


# Create your views here.
def view_cart(request):
    return render(request, "cart/cart.html")


def add_to_cart(request, item_id):

    product = Product.objects.get(pk=item_id)
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    cart = request.session.get('cart', {})

    if item_id in list(cart.keys()):
        # if the item already exists, increase the quantity of that item
        cart[item_id] += quantity
        messages.success(request, f'Added {product.name} has been added to your cart')
    else:
        # if the item doesn't exist, create this quantity
        cart[item_id] = quantity
        messages.success(request, f'Added {product.name} has been added to your cart')

    request.session['cart'] = cart
    return redirect(redirect_url)


def update_cart(request, item_id):

    quantity = int(request.POST.get('quantity'))
    cart = request.session.get('cart', {})

    if quantity > 0:
        cart[item_id] = quantity
    else:
        cart.pop(item_id)

    request.session['cart'] = cart
    return redirect(reverse('view_cart'))


def remove_from_cart(request, item_id):

    cart = request.session.get('cart', {})
    cart.pop(item_id)

    print("An item has been removed from your cart")

    request.session['cart'] = cart
    return redirect(reverse('view_cart'))