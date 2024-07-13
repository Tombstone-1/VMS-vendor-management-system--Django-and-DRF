from django.db import models
from django.db.models import Avg
from django.db.models.signals import post_save
from django.dispatch import receiver
from datetime import timedelta


class Vendor(models.Model):
    name = models.CharField(max_length=50)
    contact_details = models.TextField()
    address = models.TextField()
    vendor_code = models.CharField(max_length=50, blank=False, unique=True, primary_key=True)
    on_time_delivery_rate = models.FloatField(default=0.0)
    quality_rating_avg = models.FloatField(default=0.0)
    average_response_time = models.FloatField(default=0.0)
    fulfillment_rate = models.FloatField(default=0.0)

    def __str__(self):
        return self.vendor_code
    

class Purchase_Order(models.Model):

    po_number = models.CharField(max_length=50, blank=False, null=False, unique=True, primary_key=True)
    vendor = models.ForeignKey(Vendor, null=True, on_delete=models.SET_NULL)
    order_date = models.DateTimeField(auto_now_add=True)
    delivery_date = models.DateTimeField(blank=True, null=True)
    items = models.JSONField()
    quantity = models.IntegerField()
    status = models.CharField(max_length=20)
    quality_rating = models.FloatField(blank=True, null=True)
    issue_date = models.DateTimeField(auto_now_add=True)
    acknowledgment_date = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.po_number
    

class Historical_Performance(models.Model):
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE)
    date = models.DateTimeField()
    on_time_delivery_rate = models.FloatField(default=0.0)
    quality_rating_avg = models.FloatField(default=0.0)
    average_response_time = models.FloatField(default=0.0)
    fulfillment_rate = models.FloatField(default=0.0)

    def __str__(self):
        return self.vendor

@receiver(post_save, sender=Purchase_Order)
def update_delivery_time(sender, instance, **kwargs):
    if instance.status == 'pending' and instance.delivery_date is None:
        if instance.acknowledgement_date is None:
            instance.delivery_date= instance.issue_date + timedelta(days=10)
        else:
            instance.delivery_date=instance.acknowledgement_date + timedelta(days=7)

        instance.save()


@receiver(post_save, sender=Purchase_Order)
def onTime_delivery_rate(sender, instance, **kwargs):
    if instance.status == 'completed':
        completed_orders = Purchase_Order.objects.filter(vendor=instance.vendor, status='completed')
        timed_deliveries = completed_orders.filter(delivery_date__lte= instance.delivery_date) #lte=lessthanequal

        ONDR = timed_deliveries.count() / completed_orders.count()
        instance.vendor.on_time_delivery_rate = ONDR if ONDR is not None else 0.0
    
        instance.save()


@receiver(post_save, sender=Purchase_Order)
def quality_rating_average(sender, instance, **kwargs):
    completed_PO_rating = Purchase_Order.objects.filter(vendor=instance.vendor, status='completed')
    average_quality_rating = completed_PO_rating.aggregate(Avg('quality_rating')) ['quality_rating_avg']
    instance.vendor.quality_rating_avg = average_quality_rating if average_quality_rating is not None else 0.0
    instance.save()




        