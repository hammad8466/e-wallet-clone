from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import CustomUser, Wallet

@receiver(post_save, sender=CustomUser)
def create_user_wallet(sender, instance, created, **kwargs):
    if created:
        Wallet.objects.create(user=instance)

@receiver(post_save, sender=CustomUser)
def save_user_wallet(sender, instance, **kwargs):
    instance.wallet.save()
