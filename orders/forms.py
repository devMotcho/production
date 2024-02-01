from django import forms

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