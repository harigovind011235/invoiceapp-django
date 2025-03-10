from django.contrib import admin
from .models import Vendor, Customer, Invoice, CustomUser

# Register your models here.
admin.site.register(Vendor)
admin.site.register(Customer)
admin.site.register(Invoice)
admin.site.register(CustomUser)