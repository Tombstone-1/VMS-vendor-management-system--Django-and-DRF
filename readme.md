Project Name = Vendor Management System with Performance Metrics

Objective

Develop a Vendor Management Systemusing Django and Django REST Framework. This
system will handle vendor profiles, track purchase orders, and calculate vendor performance
metrics.

# Features

1. Vendor Profile Management:
   - Create, retrieve, update, and delete vendor profiles.
   - Calculate and display vendor performance metrics.

2. Purchase Order Tracking:
   - Create, retrieve, update, and delete purchase orders.
   - Track delivery status, items, quantity, and other details.

3. Vendor Performance Evaluation:
   - Calculate performance metrics, including on-time delivery rate, quality rating average, average response time, and fulfillment rate.
   - Historical performance tracking for trend analysis.

# Technical Requirements

- Django 
- Django REST Framework
- Token-based authentication
- PEP 8 compliant code
- Comprehensive data validations
- Django ORM for database interactions

# Installations

1. Create and activate a virtual enviroment:
    python -m venv virtenv
    virtenv\scripts\activate  (for windows)
    source virtenv/scripts/activate (for git bash)

2. Install dependencies:
    Package             Version
    asgiref             3.8.1
    Django              5.0.7
    djangorestframework 3.15.2
    pip                 24.1.2
    sqlparse            0.5.0
    tzdata              2024.1

    Or
    pip install -r requirements.txt

3. Run migrations:
    python manage.py makemigrations api
    python manage.py migrate

4. Create Super User for Authentication
    python manage.py createsuperuser

5. Run server
    python manage.py runserver

# API endpoints
    http://127.0.0.1:8000/api/vendors/ 
    http://127.0.0.1:8000/api/vendors/<str:vendor_id>/
    http://127.0.0.1:8000/api/vendors/<str:vendor_id>/performance

    http://127.0.0.1:8000/api/purchase_orders/
    http://127.0.0.1:8000/api/purchase_orders/<str:pk>/  
    http://127.0.0.1:8000/api/purchase_orders/<str:pk>/acknowledge/ 

# endpoint for Vendor.

1. Create Vendors
    url = http://127.0.0.1:8000/api/vendors/
    request = POST
        {
            "vendor_code": "VND-001",
            "name": "vendor01",
            "contact_details": "vendor details01",
            "address": "vendor address01",
        }

2. list vendors
    url = http://127.0.0.1:8000/api/vendors/
    request = GET
    
3. Update vendors
    url = http://127.0.0.1:8000/api/vendors/<str:vendor_id>/
    request = GET, PUT, DELETE

4. Performance Review of Vendor
    url = http://127.0.0.1:8000/api/vendors/<str:vendor_id>/performance
    requesy = GET

# endpoints for Purchase Order Tracking

1. Create Purchase Order
    url = http://127.0.0.1:8000/api/purchase_orders/
    request = POST
        {
            "po_number": "PO-001",
            "items": {
                "items": "items1"
            },
            "quantity": 1,
            "status": "Pending",
            "vendor": "VND-001"
        }  

2. list purchase Orders
    url = http://127.0.0.1:8000/api/purchase_orders/
    request = GET
    
3. Update purchase orders
    url = http://127.0.0.1:8000/api/purchase_orders/<str:po_id>/
    request = GET, PUT, DELETE

4. Acknowledge of Purchase order by Vendor
    url = http://127.0.0.1:8000/api/vendors/<str:po_id>/performance
    requesy = POST

