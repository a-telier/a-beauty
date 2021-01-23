from django.shortcuts import render, reverse, redirect
from django.contrib import messages

from .forms import OrderForm
from .models import Order, OrderLineItem

from products.models import Product

from profiles.models import UserProfile
# from profiles.forms import UserProfileForm

# from cart.contexts import cart_contents

import stripe
import json

# Create your views here.

def checkout (request):
    cart = request.session.get('cart', {})
    if not cart:
        messages.error(request, "Hold your horses, there is nothing on your cart right now")
        return redirect(reverse('products'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form' : order_form,
    }
    return render(request, template, context)