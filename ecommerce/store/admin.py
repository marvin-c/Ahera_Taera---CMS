from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin
from .models import *

# Register your models here.
class CustomOrderItemAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        if request.user.username == 'mcjev':
            return False
        return True

class CustomOrderAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        if request.user.username == 'mcjev':
            return False
        return True

admin.site.register(Customer)
admin.site.register(Product)
admin.site.register(Order, CustomOrderAdmin) 
admin.site.register(OrderItem, CustomOrderItemAdmin)
admin.site.register(ShippingAddress)