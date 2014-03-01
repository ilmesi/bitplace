from django.contrib import admin

# Register your models here.
from .models import Product, Account, Payment

class ProductAdmin(admin.ModelAdmin):
    pass

class PaymentAdmin(admin.ModelAdmin):
    pass

class AccountAdmin(admin.ModelAdmin):
    pass


admin.site.register(Product, ProductAdmin)
admin.site.register(Account, AccountAdmin)
admin.site.register(Payment, PaymentAdmin)

