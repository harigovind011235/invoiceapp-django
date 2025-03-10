from django.db.models.signals import post_save, pre_delete
from django.dispatch import receiver
from .models import CustomUser, Vendor, Customer
 
 
@receiver(post_save, sender=CustomUser) 
def create_vendor_or_customer(sender, instance, created, **kwargs):
    if created:
        if instance.role == 'vendor':
            Vendor.objects.create(user=instance, name=instance.username, contact_email=instance.email)
        elif instance.role == 'customer':
            Customer.objects.create(user=instance, name=instance.username, contact_email=instance.email)
  
