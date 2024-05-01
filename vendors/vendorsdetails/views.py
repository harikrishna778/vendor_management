from django.utils import timezone
from rest_framework import generics
from rest_framework import views, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from .models import PurchaseOrder, HistoricalPerformance
from .models import Vendor
from .serializers import VendorSerializer, PurchaseOrderSerializer, HistoricalPerformanceSerializer


class PermissionClass:
    permission_classes = [IsAuthenticated]


class VendorListView(PermissionClass, generics.ListCreateAPIView):
    queryset = Vendor.objects.all()
    serializer_class = VendorSerializer


class VendorRetrieveUpdateDestroyAPIView(PermissionClass, generics.ListCreateAPIView):
    queryset = Vendor.objects.all()
    serializer_class = VendorSerializer


class PurchaseOrderListView(PermissionClass, generics.ListCreateAPIView):
    serializer_class = PurchaseOrderSerializer

    def get_queryset(self):
        queryset = PurchaseOrder.objects.all()
        vendor_id = self.request.query_params.get('vendor_id', None)
        if vendor_id:
            queryset = queryset.filter(vendor__id=vendor_id)
        return queryset


class PurchaseOrderRetrieveUpdateDestroyAPIView(PermissionClass, generics.ListCreateAPIView):
    queryset = PurchaseOrder.objects.all()
    serializer_class = PurchaseOrderSerializer


class HistoricalPerformanceListView(PermissionClass, generics.ListCreateAPIView):
    queryset = HistoricalPerformance.objects.all()
    serializer_class = HistoricalPerformanceSerializer


class HistoricalPerformanceAPIView(PermissionClass, views.APIView):
    serializer_class = HistoricalPerformanceSerializer

    def get(self, request, pk):
        # Retrieve historical performance metrics for the vendor with ID=pk
        queryset = HistoricalPerformance.objects.filter(vendor_id=pk)
        serializer = self.serializer_class(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class AcknowledgePurchaseOrderAPIView(PermissionClass, views.APIView):

    def post(self, request, po_id):
        try:
            purchase_order = PurchaseOrder.objects.get(pk=po_id)
        except PurchaseOrder.DoesNotExist:
            return Response({'error': 'Purchase order not found'}, status=status.HTTP_404_NOT_FOUND)

        purchase_order.acknowledgment_date = timezone.now()
        purchase_order.save()

        # Return success response
        serializer = PurchaseOrderSerializer(purchase_order)
        return Response(serializer.data, status=status.HTTP_200_OK)
