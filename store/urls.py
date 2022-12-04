import imp
from django.urls import path

from .views import (
    create_supplier,
    create_buyer,
    create_season,
    create_drop,
    create_product,
    create_order,
    create_delivery,
    SupplierListView,
    BuyerListView,
    SeasonListView,
    DropListView,
    ProductListView,
    OrderListView,
    DeliveryListView,
    invoice_details,
    invoice_list, customer_invoices,
    product_details,product_list, customer_products,
    supplier_list, supplier_details,
    buyer_list, buyer_details,
    order_list, order_details,customer_orders,
    category_list, category_details, customer_categories,
    buyerCounts, productCounts,
    deliveryCounts, supplierCounts,
    orderCounts, total_orders, total_stock, total_price,
)

from store import views

urlpatterns = [

    path('products/', product_list),
    path('products/<int:id>', product_details),
    path('products/customers/<int:customerId>', customer_products),


    path('suppliers/', supplier_list),
    path('suppliers/<int:id>', supplier_details),

    path('buyers/', buyer_list),
    path('buyers/<int:id>', buyer_details),

    path('orders/', order_list),
    path('orders/<int:id>', order_details),
    path('orders/customers/<int:customerId>', customer_orders),


    path('invoices/', invoice_list),
    path('invoices/<int:id>', invoice_details),
    path('invoices/customers/<int:customerId>', customer_invoices),


    path('categories/', category_list),
    path('categories/<int:id>', category_details),
    path('categories/customers/<int:customerId>', customer_categories),


    path('ordercount/', orderCounts),
    path('buyercount/', buyerCounts),

    path('suppliercount/', supplierCounts),
    path('productcount/', productCounts),

    path('deliverycount/', deliveryCounts),

    path('totalstock/', total_stock),

    path('totalprice/', total_price),

    path('create-supplier/', create_supplier, name='create-supplier'),
    path('create-buyer/', create_buyer, name='create-buyer'),
    path('create-season/', create_season, name='create-season'),
    path('create-drop/', create_drop, name='create-drop'),
    path('create-product/', create_product, name='create-product'),
    path('create-order/', create_order, name='create-order'),
    path('create-delivery/', create_delivery, name='create-delivery'),

    path('supplier-list/', SupplierListView.as_view(), name='supplier-list'),
    path('buyer-list/', BuyerListView.as_view(), name='buyer-list'),
    path('season-list/', SeasonListView.as_view(), name='season-list'),
    path('drop-list/', DropListView.as_view(), name='drop-list'),
    path('product-list/', ProductListView.as_view(), name='product-list'),
    path('order-list/', OrderListView.as_view(), name='order-list'),
    path('delivery-list/', DeliveryListView.as_view(), name='delivery-list'),
]
