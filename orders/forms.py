from django import forms
from django.forms import modelformset_factory
from .models import Order, Position

CHART_CHOICES = (
    ('#1', 'Gráfico de Barras'),
    ('#2', 'Gráfico de Pizza'),
    ('#3', 'Gráfico de Linhas'),
)

RESULT_CHOICES = (
    ('#1', 'Transação'),
    ('#2', 'Data de Encomenda'),
)

class OrdersSearchForm(forms.Form):
    """ Não está diretamente relacionado a nenhum modelo, herda então de forms """
    date_from = forms.DateTimeField(widget=forms.DateInput(attrs={'type': 'date'}))
    date_to = forms.DateTimeField(widget=forms.DateInput(attrs={'type': 'date'}))
    chart_type = forms.ChoiceField(choices=CHART_CHOICES)
    results_by = forms.ChoiceField(choices=RESULT_CHOICES)


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['client', 'delivery_date']
        widgets ={
            'delivery_date': forms.DateInput(attrs={'type': 'date'}),
        }

class PositionForm(forms.ModelForm):
    class Meta:
        model = Position
        fields = ['product', 'quantity']

PositionFormSet = modelformset_factory(
    Position, fields=('product', 'quantity'), extra=1
)