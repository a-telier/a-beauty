from django.shortcuts import render, reverse, redirect, get_object_or_404
from django.contrib import messages
from django.conf import settings

#   Modules from other apps
from products.models import Product
from .forms import OrderForm
from .models import Order, OrderLineItem

from profiles.models import UserProfile
# from profiles.forms import UserProfileForm

from cart.context import cart_contents

import stripe
import json

# Create your views here.


def checkout(request):
    STRIPE_PUBLIC_KEY = settings.STRIPE_PUBLIC_KEY
    STRIPE_SECRET_KEY = settings.STRIPE_SECRET_KEY

    # cart = request.session.get('cart', {})

    #   prevents the user from manually accessing checkout by typing in url
    if request.method == 'POST':
        cart = request.session.get('cart', {})

        form_data = {
            'full_name': request.POST['full_name'],
            'email': request.POST['email'],
            'phone_number': request.POST['phone_number'],
            'address': request.POST['address'],
            'postcode': request.POST['postcode'],
            'city': request.POST['city'],
            'country': request.POST['country'],
        }

        order_form = OrderForm(form_data)

        if order_form.is_valid():
            order = order_form.save()
            # pid = request.POST.get('client_secret').split('_secret')[0]
            # order.stripe_pid = pid

            # order.original_cart = json.dumps(cart)
            # order.save()

            #   iterate through cart items
            for item_id, item_data in cart.items():
                try:
                    #   IF the item exists:
                    #   get product ID from cart
                    #   create one object per line
                    product = Product.objects.get(id=item_id)
                    order_line_item = OrderLineItem(
                        order=order,
                        product=product,
                        quantity=item_data,
                    )

                    order_line_item.save()

                except Product.DoesNotExist:
                    #   IF the item does NOT exist:
                    messages.error(request, (
                        "One of the products in your cart wasn't "
                        "found in our database. "
                        "Please contact us for assistance!")
                    )
                    order.delete()
                    return redirect(reverse('view_cart'))

            #   Save the information to the User's profile
            request.session['save_info'] = 'save-info' in request.POST
            return redirect(reverse('checkout_success', args=[order.order_number]))

        else:
            messages.error(request, 'There was an error processing your form. \
                Please review the information you entered.')

    else:
        cart = request.session.get('cart', {})
        if not cart:
            messages.error(request, "Hold your horses, there is nothing on your cart \
                right now. Let's go do some shopping..")
            return redirect(reverse('products'))

        current_cart = cart_contents(request)
        grand_total = current_cart['grand_total']
        stripe_total = round(grand_total * 100)
        stripe.api_key = STRIPE_SECRET_KEY

        intent = stripe.PaymentIntent.create(
            amount=stripe_total,
            currency=settings.STRIPE_CURR,
        )

        print('Code trying to make payment')

        order_form = OrderForm()

    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': STRIPE_PUBLIC_KEY,
        'client_secret': intent.client_secret,
    }
    return render(request, template, context)


def checkout_success(request, order_number):
    save_info = request.session.get('save_info')
    order = get_object_or_404(Order, order_number=order_number)

    # if request.user.is_authenticated:
    #     profile = UserProfile.objects.get(user=request.user)
    #     # Attach the user's profile to the order
    #     order.user_profile = profile
    #     order.save()

    #     # Save the user's info
    #     if save_info:
    #         profile_data = {
    #             'default_phone_number': order.phone_number,
    #             'default_email': order.email,
    #             'default_country': order.country,
    #             'default_postcode': order.postcode,
    #             'default_city': order.city,
    #             'default_address': order.address,
    #         }

    #         user_profile_form = UserProfileForm(profile_data, instance=profile)
    #         if user_profile_form.is_valid():
    #             user_profile_form.save()

    messages.success(request, f'We have processed your order. \
        Your order number is {order_number}. \
            You will receive a confirmation to your registered email, \
                 {order.email}, within the next minutes.')

    if 'cart' in request.session:
        del request.session['cart']

    template = 'checkout/checkout_success.html'
    context = {
        'order': order,
    }

    return render(request, template, context)
