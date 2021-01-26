from django.http import HttpResponse

#   Modules from other apps
from .models import Order, OrderLineItem
from products.models import Product

import json
import time


class Stripe_Handler:
    def __init__(self, request):
        self.request = request

    def handle_event(self, event):
        return HttpResponse(
            content=f'Web hook received: {event["type"]}',
            status=200)

    #   Sent each time a user succeeds a payment process
    def handle_payment_intent_succeeded(self, event):

        # store payment intent
        intent = event.data.object
        pid = intent.id
        cart = intent.metadata.cart
        save_info = intent.metadata.save_info

        billing_details = intent.charges.data[0].billing_details
        shipping_details = intent.shipping
        grand_total = round(intent.charges.data[0].amount/100, 2)

        #   if field comes back empty, this will be stored as None
        for field, value in shipping_details.address.items():
            if value == "":
                shipping_details.address[field] = None

        #   if the order does not exist
        order_exists = False
        #   creating a delay by running at least 5 times
        attempt = 1
        while attempt <= 5:
            try:
                order = Order.objects.get(
                    #   i here allows the field to be non case sensitive
                    full_name__iexact=shipping_details.name,
                    email__iexact=billing_details.email,
                    phone_number__iexact=shipping_details.phone,

                    country__iexact=shipping_details.address.country,
                    postcode__iexact=shipping_details.address.postal_code,
                    city__iexact=shipping_details.address.city,
                    address__iexact=shipping_details.address.line1,

                    grand_total=grand_total,
                    original_bag=cart,
                    stripe_pid=pid,
                )
                #   if the order is found, break the loop 
                order_exists = True
                break

            except Order.DoesNotExist:
                attempt += 1
                time.sleep(1)

        if order_exists:
            return HttpResponse(
                content=f'Webhook received: {event["type"]} | SUCCESS: Verified order already in database',
                status=200)
        else:
            order = None
            try:
                order = Order.objects.create(
                    full_name=shipping_details.name,
                    email=billing_details.email,
                    phone_number=shipping_details.phone,

                    address=shipping_details.address.line1,
                    postcode=shipping_details.address.postal_code,
                    city=shipping_details.address.city,
                    country=shipping_details.address.country,

                    original_bag=cart,
                    stripe_pid=pid,
                )
                for item_id, item_data in json.loads(cart).items():
                    product = Product.objects.get(id=item_id)
                    order_line_item = OrderLineItem(
                        order=order,
                        product=product,
                        quantity=item_data,
                    )
                    order_line_item.save()

            except Exception as e:
                if order:
                    order.delete()

                return HttpResponse(
                    content=f'Webhook received: {event["type"]} | ERROR: {e}',
                    status=500)

        return HttpResponse(
            content=f'Webhook received: {event["type"]} | SUCCESS: Created order in webhook',
            status=200)

    #   Sent each time a payment fails
    def handle_payment_intent_failed(self, event):
        return HttpResponse(
            content=f'Payment Failed Web hook received: {event["type"]}',
            status=200)
