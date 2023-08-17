from django.contrib import admin

from entities.models import Client, Branch, Product, Inventory

admin.site.register(Client)
admin.site.register(Branch)
admin.site.register(Product)
admin.site.register(Inventory)


