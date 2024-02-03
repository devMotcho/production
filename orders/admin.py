from django.contrib import admin

from .models import Position, Order, CSV


admin.site.register(Position)
admin.site.register(Order)
admin.site.register(CSV)
