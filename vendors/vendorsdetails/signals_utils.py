from datetime import date, timedelta

from django.db.models import Avg
from django.db.models import F


def calculate_vendor_performance_metrics(vendor, model):
    completed_orders = vendor.purchase_orders.filter(status='completed')

    total_completed_orders = completed_orders.count()
    on_time_delivered_orders = completed_orders.filter(
        delivery_date__lte=F('acknowledgment_date')
    ).count()
    vendor.on_time_delivery_rate = (
                                           on_time_delivered_orders / total_completed_orders
                                   ) * 100 if total_completed_orders != 0 else 0

    vendor.quality_rating_avg = completed_orders.aggregate(Avg('quality_rating'))['quality_rating__avg'] or 0

    acknowledged_orders = completed_orders.exclude(acknowledgment_date__isnull=True)
    response_time_sum = acknowledged_orders.annotate(
        response_time=F('acknowledgment_date') - F('issue_date')
    ).aggregate(
        Avg('response_time')
    )['response_time__avg'] or timedelta(seconds=0)

    vendor.average_response_time = response_time_sum.total_seconds() / acknowledged_orders.count() if acknowledged_orders.count() != 0 else 0

    successful_orders = completed_orders.filter(quality_rating__isnull=False)
    vendor.fulfillment_rate = (
                                      successful_orders.count() / total_completed_orders
                              ) * 100 if total_completed_orders != 0 else 0

    vendor.save()

    model.objects.create(
        vendor=vendor,
        date=date.today(),
        on_time_delivery_rate=vendor.on_time_delivery_rate,
        quality_rating_avg=vendor.quality_rating_avg,
        average_response_time=vendor.average_response_time,
        fulfillment_rate=vendor.fulfillment_rate
    )
