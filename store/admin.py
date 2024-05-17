from django.contrib import admin

from .models import (
    Supplier,
    Buyer,
    Category,
    Product,
    Order,
    Delivery,
    OrderProducts,
    Damages,
    StoreActivity
)


class SupplierAdmin(admin.ModelAdmin):
    list_display = ['user', 'name', 'address', 'created_date']


class BuyerAdmin(admin.ModelAdmin):
    list_display = ['user', 'name', 'address', 'created_date']


admin.site.register(Supplier)
admin.site.register(Buyer)
admin.site.register(Product)
admin.site.register(Order)
admin.site.register(Delivery)
admin.site.register(Category)
admin.site.register(OrderProducts)
admin.site.register(Damages)
admin.site.register(StoreActivity)
