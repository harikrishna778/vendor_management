from django.urls import path
from .views import VendorListView, PurchaseOrderListView, HistoricalPerformanceListView, \
    VendorRetrieveUpdateDestroyAPIView, PurchaseOrderRetrieveUpdateDestroyAPIView, HistoricalPerformanceAPIView, \
    AcknowledgePurchaseOrderAPIView

urlpatterns = [
    path('vendors/', VendorListView.as_view(), name='vendors_list'),
    path('vendor/<int:pk>', VendorRetrieveUpdateDestroyAPIView.as_view(), name='vendor_get_update_delete'),
    path('purchase_orders/', PurchaseOrderListView.as_view(), name='purchase_order_list'),
    path('purchase_order/<int:pk>', PurchaseOrderRetrieveUpdateDestroyAPIView.as_view(),
         name='purchase_order_get_update_delete'),

    path('historic_performances/', HistoricalPerformanceListView.as_view(), name='historical_performances_list'),
    path('vendors/<int:pk>/performance/', HistoricalPerformanceAPIView.as_view(),
         name='historical_performance_get_update_delete'),
    path('purchase_orders/<int:po_id>/acknowledge/', AcknowledgePurchaseOrderAPIView.as_view(),
         name='acknowledge-purchase-order'),

]
