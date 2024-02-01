from django.shortcuts import render

from product.models import Inventary, Product, ProductionOrder, Production
from human.models import Employee
# Create your views here.
def home(request):
    """
    Pagina de navegação
    """
    # Inventary
    inventary = Inventary.objects.filter()
    inv_count = inventary.count()
    product = Product.objects.filter()
    product_count = product.count()    
    
    
    # Human Resorces
    employees = Employee.objects.filter()
    employees_count = employees.count()

    #Produção
    production_order = ProductionOrder.objects.filter()
    production_order_count = production_order.count()

    productions = Production.objects.filter()
    productions_count = productions.count()

    context = {
        'product_count':product_count,
        'inv_count':inv_count,
        'employees_count': employees_count,
        'order' : production_order_count,
        'productions_count': productions_count
    }
    return render(request, 'dashboard/home.html', context)