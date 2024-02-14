from django.shortcuts import render, redirect
from django.contrib import messages
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

import pandas as pd

from .models import Employee, Profile
from .forms import EmployeeForm
from product.models import Production, ProductionOrder
from .utils import get_employee_by_id, get_prod_order_by_id


# Gerir Users
def loginPage(request):
    """Verificar se o user já se encontra logado, se for o caso não pode aceder a esta pagina novamente"""
    if request.user.is_authenticated:
        return redirect('dashboard:home')

    if request.method == 'POST':
        username = request.POST.get('username').lower()
        password = request.POST.get('password')

        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, 'User Not Found!', 'alert-warning alert-dismissible')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('dashboard:home')
        else:
            messages.error(request, 'As credênciais estão erradas!', 'alert-warning alert-dismissible')

    context = {}

    return render(request, 'human/login.html', context)

def logoutUser(request):
    logout(request)
    return redirect('human:login')





# Gerir funcionários
def employeesList(request):
    employees = Employee.objects.filter()
    form = EmployeeForm()
    if request.method == 'POST':
        form = EmployeeForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            messages.success(request, 'Funcionário adicionado com sucesso!', 'alert-success alert-dismissible')
        else:
            messages.error(request, 'Erro ao Validar o Formulário!', 'alert-warning alert-dismissible')

    context= {
        'objects':employees,
        'form': form,
    }
    return render(request, 'human/list.html', context)

def employeeCreate(request):
    form = EmployeeForm()
    if request.method == 'POST':
        form = EmployeeForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Funcionário adicionado com sucesso!', 'alert-success alert-dismissible')
            return redirect('human:list')
    
    context = {'form':form}
    return render(request, 'human/create.html', context)

def employeeUpdate(request, pk):
    employee = get_object_or_404(Employee, id=pk)
    form = EmployeeForm(instance=employee)
    if request.method == 'POST':
        form = EmployeeForm(request.POST, request.FILES, instance=employee)
        if form.is_valid():
            form.save()
            messages.success(request, 'Funcionário modificado com sucesso!', 'alert-success alert-dismissible')
            return redirect('human:view', pk=employee.id)

    context = {
        'employee':employee,
        'form':form,
    }
    return render(request, 'human/update.html', context)

def employeeDelete(request, pk):
    employee = get_object_or_404(Employee, id=pk)
    if request.method == 'POST':
        employee.delete()
        messages.success(request, 'Funcionário adicionado com sucesso!', 'alert-success alert-dismissible')
        return redirect('human:list')
    
    context = {
        'obj':employee,
    }

    return render(request, 'delete.html', context)

def employeeView(request, pk):
    productions_df = None
    prod_product_df = None
    result = None

    employee = Employee.objects.get(id=pk)
    productions = Production.objects.filter(employee=employee)

    productions_df = pd.DataFrame(productions.values())
    productions_df['employee_id'] = productions_df['employee_id'].apply(get_employee_by_id)
    productions_df['production_order_id'] = productions_df['production_order_id'].apply(get_prod_order_by_id)
    productions_df['date'] = productions_df['date'].apply(lambda x: x.strftime('%Y-%m-%d'))
    productions_df.rename({'id':'Prod', 'production_order_id':'Ordem Prod', 'employee_id':'Funcionario', 'quantity':'Quantidade', 'time':'Tempo de Prod', 'date': 'data'}, axis=1, inplace=True)

    prod_product_data = []
    for production in productions:
        prod_product = {
            'Ordem Prod': production.production_order.prod_order_id,
            'Produto': production.production_order.product,
        }
        prod_product_data.append(prod_product)

    prod_product_df = pd.DataFrame(prod_product_data)
    result = pd.merge(productions_df, prod_product_df, on='Ordem Prod')
        


    print(productions_df)
    print('*********')
    print(prod_product_df)
    print('*********')
    print(result)

    productions_df = productions_df.to_html()
    result = result.to_html()

    context = {
        'obj':employee,
        'productions':productions,
        'productions_df':productions_df,
        'result':result,
    }
    return render(request, 'human/view.html', context)



