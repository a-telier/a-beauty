#   signals sent to django after something is saved or deleted
from django.db.models.signals import post_save, post_delete

#   allows to receive the signals
from django.dispatch import receiver

from .models import OrderLineItem


#   update order total
@receiver(post_save, sender=OrderLineItem)
def update_on_save(sender, instance, created, **kwargs):
    instance.order.update_total()

#   delete order total
@receiver(post_delete, sender=OrderLineItem)
def update_on_delete(sender, instance, **kwargs):
    instance.order.update_total()
