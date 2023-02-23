from django.contrib import admin

from . import models

@admin.register(models.Product)
class ProductAdmin(admin.ModelAdmin):
    list_per_page = 10
    list_display = [
        "title",
        "description",
        "price",
        "inventory",
        "inventory_status", 
        "inventory_value",
        "last_update",
        "collection"
    ]

    def inventory_value(self, product):
        return product.inventory * product.price

    @admin.display(ordering='inventory')
    def inventory_status(self, product):
        if product.inventory < 10:
            return 'Low'
        return 'OK'
    



@admin.register(models.Collection)
class CollectionAdmin(admin.ModelAdmin):
    list_per_page = 10

@admin.register(models.Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'membership', 'gender']
    list_editable = ['membership', 'gender']
    list_per_page = 10
    ordering = ['first_name','last_name']
    search_fields = ['first_name__startswith', 'last_name__startswith']

@admin.register(models.Address)
class AddressAdmin(admin.ModelAdmin):
    list_per_page = 10

@admin.register(models.Order)
class OrderAdmin(admin.ModelAdmin):
    list_per_page = 10

