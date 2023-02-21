from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin
from .models import *

# Register your models here.

# Admin to restrict add permission on order items table
class CustomOrderItemAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        if request.user.username == 'mcjev':
            return False
        return True

# Admin to restrict add persmission on order table
class CustomOrderAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        if request.user.username == 'mcjev':
            return False
        return True

admin.site.site_header = 'Welcome to Ahera Taera Administration Dashboard'
admin.site.site_title = 'Welcome to Ahera Taera Administration'
admin.site.register(Customer)
admin.site.register(Product)
admin.site.register(Order, CustomOrderAdmin) 
admin.site.register(OrderItem, CustomOrderItemAdmin)
admin.site.register(ShippingAddress)