from django import forms
from django.forms import BaseModelFormSet
from .models import Product, Production, ProductionOrder

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'


class DateInput(forms.DateInput):
    input_type = 'date'

class ProductionForm(forms.ModelForm):
    class Meta:
        model = Production
        fields = '__all__'
        widgets = {
            'date': DateInput(),
        }

class BaseProductionFormSet(BaseModelFormSet):
    def __init__(self, *args, **kwargs):
        super(BaseProductionFormSet, self).__init__(*args, **kwargs)
        self.queryset = Production.objects.none()

class ProductionOrderForm(forms.ModelForm):
    class Meta:
        model = ProductionOrder
        fields = ['product', 'quantity_ordered']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        #Excluir os produtos que já tem ordens de produção
        existing_products = ProductionOrder.objects.values_list('product', flat=True)
        self.fields['product'].queryset = Product.objects.exclude(id__in=existing_products)
