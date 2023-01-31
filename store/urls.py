from django.urls import path
from .views import (
    twilio,
    ProductListCreateView,
    ProductRetreiveUpdateDeleteView,
    CategoryListCreateView,
    CategoryRetreiveUpdateDeleteView,
    order_list,
    order_details,
    receipt_list,
    receipt_details,
    invoice_list,
    invoice_details,
    
    productCounts,
    buyerCounts, 
    deliveryCounts, 
    supplierCounts,
    orderCounts, 
    total_orders,
    total_stock, 
    total_price,

    categoryProducts,
    
    # invoice_details,
    # invoice_list, customer_invoices,
    # product_details, customer_products,
    # supplier_list, supplier_details,
    # buyer_list, buyer_details,
    # order_list, order_details,customer_orders,
    # category_list, category_details, customer_categories,
    # buyerCounts, productCounts,
    # deliveryCounts, supplierCounts,
    # orderCounts, total_orders, total_stock, total_price,
)


app_name = 'store_api'

urlpatterns = [
    path('twilio/', twilio),
    path('products/', ProductListCreateView.as_view(), name='listcreateproducts'),
    path('products/<int:pk>/', ProductRetreiveUpdateDeleteView.as_view(), name='detailupdatedeleteproducts'),
    path('categories/', CategoryListCreateView.as_view(), name='listcreatecategories'),
    path('categories/<int:pk>/', CategoryRetreiveUpdateDeleteView.as_view(), name='detailupdatedeletecategories'),
    path('orders/', order_list),
    path('orders/<int:id>', order_details),

    path('invoices/', invoice_list),
    path('invoices/<int:id>', invoice_details),

    path('receipts/', receipt_list),
    path('receipts/<int:id>', receipt_details),

    path('ordercount/', orderCounts),
    path('buyercount/', buyerCounts),
    path('suppliercount/', supplierCounts),
    path('productcount/', productCounts),
    path('deliverycount/', deliveryCounts),

    path('totalstock/', total_stock),
    path('totalprice/', total_price),

    path('categoryproducts/<int:id>', categoryProducts),







    # path('products/', product_list),
    # path('customer/products/<int:id>', product_details),
    # path('customer/products/customers/<int:customerId>', customer_products),

    # path('suppliers/', supplier_list),
    # path('suppliers/<int:id>', supplier_details),

    # path('buyers/', buyer_list),
    # path('buyers/<int:id>', buyer_details),

    # path('orders/', order_list),
    # path('orders/<int:id>', order_details),
    # path('orders/customers/<int:customerId>', customer_orders),

    # path('invoices/', invoice_list),
    # path('invoices/<int:id>', invoice_details),
    # path('invoices/customers/<int:customerId>', customer_invoices),


    # path('categories/', category_list),
    # path('categories/<int:id>', category_details),
    # path('categories/customers/<int:customerId>', customer_categories),


    # path('ordercount/', orderCounts),
    # path('buyercount/', buyerCounts),

    # path('suppliercount/', supplierCounts),
    # path('productcount/', productCounts),

    # path('deliverycount/', deliveryCounts),

    # path('totalstock/', total_stock),

    # path('totalprice/', total_price),

]
