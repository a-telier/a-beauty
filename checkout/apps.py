from django.apps import AppConfig


class CheckoutConfig(AppConfig):
    name = 'checkout'

    #   Importing Signals module here:
    def ready(self):
        import checkout.signals