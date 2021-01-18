from decimal import Decimal
from django.conf import settings
from django.shortcuts import render, get_object_or_404, redirect
from products.models import Product


def cart_contents(request):

    cart_items = []
    total = 0
    product_count = 0
    cart = request.session.get('cart', {})

    print(cart_items)

    for item_id, quantity in cart.items():
        product = get_object_or_404(Product, pk=item_id)
        # increment total by (quantity * item price)
        total = total + (quantity * product.price)
        # increment product_count by quantity
        product_count = product_count + quantity
        # append these elements as a cart_items object
        cart_items.append({
            'item_id': item_id,
            'quantity': quantity,
            'product': product,
        })

    if total < settings.FREE_DELIVERY_THRESHOLD:
        delivery = total * Decimal(settings.STANDARD_DELIVERY_PERCENTAGE / 100)
        free_delivery_delta = settings.FREE_DELIVERY_THRESHOLD - total
    else:
        delivery = 0
        free_delivery_delta = 0

    grand_total = delivery + total

    context = {
        'cart_items': cart_items,
        'total': total,
        'product_count': product_count,
        'delivery': delivery,
        'free_delivery_delta': free_delivery_delta,
        'free_delivery_threshold': settings.FREE_DELIVERY_THRESHOLD,
        'grand_total': grand_total,
    }

    return context
