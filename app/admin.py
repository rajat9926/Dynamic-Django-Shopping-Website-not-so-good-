from django.contrib import admin
from .models import Cart,CustomerInfo,Product,OrderPlaced

@admin.register(CustomerInfo)
class AdminCustomerInfo(admin.ModelAdmin):
    list_display= ['user','name','locality','city','zipcode','state']

@admin.register(Product)
class AdminProduct(admin.ModelAdmin):
    list_display= ['category','product_name', 'description','brand','MRP','discounted_price','images']

@admin.register(Cart)
class AdminCart(admin.ModelAdmin):
    list_display= ['user','product','quantity'] 

@admin.register(OrderPlaced)
class AdminOrderPlaced(admin.ModelAdmin):
    list_display= ['user','product','customer_info','status','ordered_date']