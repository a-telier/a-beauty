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
        'stripe_public_key': 'pk_test_51ICsfUDzMqC2yDSdRI8QLg3Z3pfj68JeCtc4VHd0Yu4IV1jZ0wWBMPbetHiiRYJCox3oBx6Yv3G9tW0ErlF6YPUp00MySU6XSI',
        'client_secret': 'test client secret',
    }
    return render(request, template, context)