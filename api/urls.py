from django.urls import path
from rest_framework.authtoken import views as rest_views
from . import views

urlpatterns = [
    # use this link to get auth token when valid username and password provided.
    path('token-auth/', rest_views.obtain_auth_token),

    # vendor
    path('vendors/', views.vendors_list),
    path('vendors/<str:vendor_id>/', views.vendors_update),

    path("vendors/<str:vendor_id>/performance/", views.vendor_performance),

    # Purchase
    path('purchase_orders/', views.purchase_order_list),
    path('purchase_orders/<str:po_id>/', views.purchase_order_update),

    path('purchase_orders/<str:po_id>/acknowledge/',
         views.PurchaseOrder_acknowledgement),
]
