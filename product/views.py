from django.shortcuts import render, redirect
from django.contrib import messages
from django.shortcuts import get_object_or_404
from django.db.models import Q
from django.forms import modelformset_factory

from .models import Product, Inventary, ProductionOrder, Production
from .forms import ProductForm, ProductionForm, BaseProductionFormSet, ProductionOrderForm



# PRODUTOS 
def productList(request):
     # Tabela com todos os dados de produtos
    q = request.GET.get('q') if request.GET.get('q') is not None else ''
    
    products = Product.objects.filter(
        Q(name__icontains=q) |
        Q(category__icontains=q)
    )
    form = ProductForm()
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Produto criado com sucesso!', 'alert-success alert-dismissible')
            return redirect('product:list')
        else:
            messages.warning(request, 'Tentativa falhada!', 'alert-info alert-dismissible')
    context = {
        'objects':products,
        'form':form,
    }
    return render(request, 'product/list.html', context)

def productCreate(request):
        # Formulário de criação de produto.
    form = ProductForm()
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Produto criado com sucesso!', 'alert-success alert-dismissible')
            return redirect('product:list')
        else:
            messages.warning(request, 'Tentativa falhada!', 'alert-info alert-dismissible')
    context = {
        'form':form,
    }
    return render(request, 'product/create.html', context)

def productUpdate(request, pk):
    product = get_object_or_404(Product, id=pk)
    form = ProductForm(instance=product)
    if request.method == 'POST':
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, 'Produto editado com sucesso!', 'alert-success alert-dismissible')
            return redirect('product:list')
        else:
            messages.warning(request, 'Tentativa falhada!', 'alert-info alert-dismissible')
    
    context = {
        'form':form,
        'obj':product,
    }
    return render(request, 'product/update.html', context)

def productDelete(request, pk):
    product = get_object_or_404(Product, id=pk)
    if request.method == 'POST':
        product.delete()
        messages.success(request, 'Product Deleted!', "alert-success alert-dismissible")
        return redirect('product:list')
    return render(request, 'product/delete.html', {'obj': product})

def productView(request, pk):
    """
    Vista de um unico produto
    quero adicionar estatisticas de cada produto
    """
    product = get_object_or_404(Product, id=pk)
    try:
        production_order = ProductionOrder.objects.get(product=product)
    except ProductionOrder.DoesNotExist:
        production_order = ProductionOrder.objects.none()
    productions = Production.objects.filter(production_order__product=product)

    
        
    context = {
        'obj':product,
        'order':production_order,
        'productions':productions
    }
    return render(request, 'product/view.html', context)




# INVENTARIO
def inventaryView(request):
    q = request.GET.get('q') if request.GET.get('q') is not None else ''
    inv = Inventary.objects.filter(
        Q(product__name__icontains=q)
    )

    context = {
        'objects' : inv,
    }
    return render(request, 'product/inventary.html', context)




#PRODUÇÃO
def productionView(request):
    q = request.GET.get('q') if request.GET.get('q') is not None else ''
    productions = Production.objects.filter(
        Q(employee__first_name__icontains=q) |
        Q(inventary__product__name__icontains=q)
    )
        # Criação do formset com base no formulário do modelo Production
    ProductionFormSet = modelformset_factory(Production, ProductionForm, extra=1, formset=BaseProductionFormSet)
    formset = ProductionFormSet(queryset=Production.objects.none())
    if request.method == 'POST':
        formset = ProductionFormSet(request.POST)
        if formset.is_valid():
            formset.save()
            return redirect('product:prod')
            messages.success(request, 'Productions added with success!', "alert-success alert-dismissible")

    context = {
        'objects': productions,
        'form':formset,
    }
    return render(request, 'product/production.html', context)


def productionEdit(request, pk):
    production = Production.objects.get(id=pk)
    form = ProductionForm(instance=production)
    if request.method == 'POST':
        form = ProductionForm(request.POST, instance=production)
        if form.is_valid():
            form.save()
            messages.success(request, 'Produção Atualizada!', 'alert-success alert-dismissible')
            return redirect('product:prod')
        else:
            messages.error(request, 'Falha na Atualização!', 'alert-warning alert-dismissible')
    context = {
        'form':form,
        'production':production,
    }
    return render(request, 'product/edit.html', context )


def productionDelete(request, pk):
    production = get_object_or_404(Production, id=pk)
    if request.method == 'POST':
        production.delete()
        messages.success(request, 'Produção Deleted!', "alert-success alert-dismissible")
        return redirect('product:prod')
    return render(request, 'product/delete.html', {'obj': production})


#Orem Produção
def productionOrderView(request):
    ordemProd = ProductionOrder.objects.filter()
    form = ProductionOrderForm()
    if request.method == 'POST':
        form = ProductionOrderForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Ordem Adicionada com sucesso!', 'alert-success alert-dismissible')

    context = {
        'objects': ordemProd,
        'form':form,

    }
    return render(request, 'product/production_order.html', context)

