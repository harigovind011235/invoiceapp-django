from rest_framework import serializers
from .models import Vendor, Customer, Invoice


class VendorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vendor
        fields = '__all__'


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = '__all__'


class InvoiceSerializer(serializers.ModelSerializer):
    
    vendor_name = serializers.ReadOnlyField(source='vendor.name')
    customer_name = serializers.ReadOnlyField(source='customer.name')
    
    class Meta:
        model = Invoice
        fields = [
            "invoice_number",
            "vendor",
            "customer",
            "service_type",
            "date",
            "related_docs",
            "subtotal",
            "discount",
            "total_amount",
            "is_cleared",
            "notes",
            "created_at",
            "updated_at",
            "vendor_name",
            "customer_name",
        ]
