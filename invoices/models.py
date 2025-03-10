from django.db import models
import uuid
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):

    ROLE_CHOICES = [
        ('admin', 'Admin'),
        ('customer', 'Customer'),
        ('vendor', 'Vendor')
    ]

    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='admin')

    def __str__(self):
        return f'{self.username}'


class Vendor(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, null=True, blank=True)
    vendor_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    contact_email = models.EmailField(unique=True)
    contact = models.CharField(max_length=10, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.name}'


class Customer(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, null=True, blank=True)
    customer_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    contact_email = models.EmailField(unique=True)
    contact = models.CharField(max_length=10, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.name}'
    

class Invoice(models.Model):

    SERVICE_TYPES = [
        ('bike_wash', 'Bike Wash'),
        ('chain_lube', 'Chain Lube'),
        ('break_replacement', 'Brake Replacement')
    ]
    
    invoice_number = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE, related_name="vendor_invoices")
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name="customer_invoices")
    service_type = models.CharField(max_length=20, choices=SERVICE_TYPES, blank=True, null=True)
    date = models.DateField(auto_now_add=True)
    related_docs = models.FileField(upload_to='file_uploads', null=True, blank=True)
    subtotal = models.DecimalField(max_digits=20, decimal_places=2, default=0.00)
    discount = models.DecimalField(max_digits=20, decimal_places=2, default=0.00)
    total_amount = models.DecimalField(max_digits=20, decimal_places=2, default=0.00, null=True, blank=True)
    is_cleared = models.BooleanField(default=False)
    notes = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        if not self.total_amount:
            self.total_amount = self.subtotal - self.discount
        super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.customer.name} - {self.invoice_number}'