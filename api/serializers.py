from rest_framework import serializers
from .models import Vendor, Purchase_Order

class Vendor_profile_serializers(serializers.ModelSerializer):
    class Meta:
        model = Vendor
        fields = '__all__'
    

class Vendor_performance_serializer(serializers.ModelSerializer):
    class Meta:
        model = Vendor
        fields = ['on_time_delivery_rate','quality_rating_avg','average_response_time','fulfillment_rate']

class Purchase_Order_Tracking_serializer(serializers.ModelSerializer):
    class Meta:
        model = Purchase_Order
        fields = '__all__'
