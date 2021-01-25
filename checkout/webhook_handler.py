from django.http import HttpResponse

class Stripe_Handler:
    def __init__(self, request):
        self.request = request

    def handle_event(self, event):
        return HttpResponse(
            content=f'Web hook received: {event['type']}',
            status=200)