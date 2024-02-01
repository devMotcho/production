from django.contrib import admin

from .models import Employee, Client, Profile

admin.site.register(Employee)
admin.site.register(Client)
admin.site.register(Profile)
