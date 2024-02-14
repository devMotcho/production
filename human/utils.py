from .models import Employee
from product.models import ProductionOrder

def get_employee_by_id(val):
    employee = Employee.objects.get(id=val)
    return employee

def get_prod_order_by_id(val):
    prod_order = ProductionOrder.objects.get(id=val)
    return prod_order

