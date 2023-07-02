from paypal.standard.ipn.signals import valid_ipn_received, invalid_ipn_received
from django.dispatch import receiver

from .models import Competition

@receiver(valid_ipn_received)
def valid_ipn_signal(sender, **kwargs):
    print("valid ipn")
    ipn = sender
    if ipn.payment_status == 'Completed':
        Competition.objects.create()

@receiver(invalid_ipn_received)
def invalide_ipn_signal(sender, **kwargs):
    print("Invalid ipn")
    ipn = sender
    if ipn.payment_status == 'Completed':
        Competition.objects.create()