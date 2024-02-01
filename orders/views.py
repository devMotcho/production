from django.shortcuts import render
from django.views.generic import ListView, DetailView
import pandas as pd

#my imports
from .models import Order, Position
from .forms import OrdersSearchForm


def search(request):
    dataframe = None


    form = OrdersSearchForm(request.POST or None)

    if request.method == 'POST':

        date_from = request.POST.get('date_from')
        date_to = request.POST.get('date_to')
        chart_type = request.POST.get('chart_type')
        results_by = request.POST.get('results_by')

        orders_qs = Order.objects.filter(
            created__date__lte=date_to, #lte = less then or equal to
            created__date__gte=date_from, #gte = Greater Then or equal to
        )
        if len(orders_qs) > 0 :
            dataframe = pd.dataframe(orders_qs.values())



    context = {
        'form':form,
        'dataframe':dataframe,
    }
    return render(request, 'orders/search.html', context)


class OrderListView(ListView):
    model = Order
    template_name = 'orders/list.html'

class OrderDetailView(DetailView):
    model = Order
    template_name = 'orders/detail.html'