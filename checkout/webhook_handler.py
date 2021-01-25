from django.http import HttpResponse


class Stripe_Handler:
    def __init__(self, request):
        self.request = request

    def handle_event(self, event):
        return HttpResponse(
            content=f'Web hook received: {event["type"]}',
            status=200)

    #   Sent each time a user succeeds a payment process
    def handle_payment_intent_succeeded(self, event):
        return HttpResponse(
            content=f'Web hook received: {event["type"]}',
            status=200)

    #   Sent each time a payment fails
    def handle_payment_intent_failed(self, event):
        return HttpResponse(
            content=f'Payment Failed Web hook received: {event["type"]}',
            status=200)
