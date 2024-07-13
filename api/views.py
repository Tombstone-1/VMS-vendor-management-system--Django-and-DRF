from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User
from rest_framework import status
from datetime import datetime

from .serializers import Vendor_profile_serializers, Vendor_performance_serializer, Purchase_Order_Tracking_serializer
from .models import Vendor, Purchase_Order

for user in User.objects.all():
    token= Token.objects.get_or_create(user=user)
    #print(token)


@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def vendors_list(request):
    if request.method == 'GET':
        queryset = Vendor.objects.all()
        serializer = Vendor_profile_serializers(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    elif request.method == 'POST':
        serializer = Vendor_profile_serializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes([IsAuthenticated])
def vendors_update(request, vendor_id):
    try:
        queryset = Vendor.objects.get(vendor_code=vendor_id)
    except Vendor.DoesNotExist:
        return Response({"warning" : "selected vendor_id data not found"},status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = Vendor_profile_serializers(queryset)
        return Response(serializer.data, status=status.HTTP_200_OK)

    elif request.method == 'PUT':
        serializer = Vendor_profile_serializers(
            instance=queryset, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        queryset.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def purchase_order_list(request):
    if request.method == 'GET':
        query = Purchase_Order.objects.all()
        serializer = Purchase_Order_Tracking_serializer(query, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    elif request.method == 'POST':
        serializer = Purchase_Order_Tracking_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes([IsAuthenticated])
def purchase_order_update(request, po_id):
    try:
        queryset = Purchase_Order.objects.get(po_number=po_id)
    except Purchase_Order.DoesNotExist:
        return Response({"warning" : "selected purchase_order_id data not found"},status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = Purchase_Order_Tracking_serializer(queryset)
        return Response(serializer.data, status=status.HTTP_200_OK)

    elif request.method == 'PUT':
        serializer = Purchase_Order_Tracking_serializer(instance=queryset, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        queryset.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def vendor_performance(request, vendor_id):
    try:
        queryset = Vendor.objects.get(vendor_code=vendor_id)
        serializer = Vendor_performance_serializer(queryset)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    except queryset.DoesNotExist:
        return Response({"warning" : "selected vendor_id data not found"},status=status.HTTP_404_NOT_FOUND) 
        
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def PurchaseOrder_acknowledgement(request, po_id):
    try:
        queryset = Purchase_Order.objects.get(po_number=po_id)
    except Purchase_Order.DoesNotExist:
        return Response({"warning" : "selected purchase_order_id data not found"},status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'POST':
        queryset.acknowledgment_date=datetime.now()
        queryset.save()
        return Response({"success" : "Acknowledge Time Updated Successfully"}, status=status.HTTP_200_OK)
                
        
