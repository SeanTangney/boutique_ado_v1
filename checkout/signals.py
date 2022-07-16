from django.db.models.signals import post_save, post_delete
from django.dispatch import reciever

from .models import OrderLineItem

@reciever(post, save, sender=OrderItem)
def update_on_save(sender, instance, created, **kwargs):
    """
    update order total on lineitem update/create
    """
    instance.order.update_total()
