from django.urls import path
from . import views

urlpatterns = [
    # vendor
    path('vendors/',views.vendors_list),
    path('vendors/<str:vendor_id>/',views.vendors_update),

    path("vendors/<str:vendor_id>/performance/",views.vendor_performance),

    # Purchase
    path('purchase_orders/', views.purchase_order_list),
    path('purchase_orders/<str:po_id>/', views.purchase_order_update),

    # Acknowledgement update
    path('purchase_orders/<str:po_id>/acknowledge/', views.PurchaseOrder_acknowledgement),
]
