from django.shortcuts import render, reverse, redirect
from django.contrib import messages
from django.conf import settings

from .forms import OrderForm
from .models import Order, OrderLineItem

from products.models import Product

from profiles.models import UserProfile
# from profiles.forms import UserProfileForm

from cart.context import cart_contents

import stripe
import json

# Create your views here.

def checkout (request):
    STRIPE_PUBLIC_KEY = settings.STRIPE_PUBLIC_KEY
    STRIPE_SECRET_KEY = settings.STRIPE_SECRET_KEY

    cart = request.session.get('cart', {})
    if not cart:
        messages.error(request, "Hold your horses, there is nothing on your cart right now")
        return redirect(reverse('products'))

    current_cart = cart_contents(request)
    grand_total = current_cart['grand_total']
    stripe_total = round(grand_total * 100)
    stripe.api_key = STRIPE_SECRET_KEY

    stripe.PaymentIntent.create(
        amount = stripe_total,
        currency = settings.STRIPE_CURR,
    )

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form' : order_form,
        'stripe_public_key': STRIPE_PUBLIC_KEY,
        'client_secret': intent.client_secret ,
    }
    return render(request, template, context)