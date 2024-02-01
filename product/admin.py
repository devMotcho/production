from django.contrib import admin

from .models import Product, Production, ProductionOrder, Inventary

admin.site.register(Product)
admin.site.register(Production)
admin.site.register(ProductionOrder)
admin.site.register(Inventary)
