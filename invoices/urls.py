from django.urls import path, include
from .views import VendorViewSet, CustomerViewSet, InvoiceViewSet
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register(r'vendors', VendorViewSet)
router.register(r'customers', CustomerViewSet)
router.register(r'invoices', InvoiceViewSet)

urlpatterns = [
    path('', include(router.urls),)
]