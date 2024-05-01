from django.contrib import admin
from django.contrib.admin import register

from .models import Vendor, PurchaseOrder, HistoricalPerformance


@register(Vendor)
class VendorAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'vendor_code')
    list_filters = ('name', 'vendor_code',)

@register(PurchaseOrder)
class PurchaseOrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'vendor')
    list_filters = ('name', 'vendor')

@register(HistoricalPerformance)
class HistoricalPerformanceAdmin(admin.ModelAdmin):
    list_display = ('id', 'vendor')
    list_filters = ('name', 'vendor')
