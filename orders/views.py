from django.shortcuts import render
from django.views.generic import ListView, DetailView
import pandas as pd

#my imports
from .models import Order, Position
from .forms import OrdersSearchForm
from .utils import get_client_from_id, get_salesman_from_id


def search(request):
    dataframe = None
    positions_df = None
    merged_df = None


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
            dataframe = pd.DataFrame(orders_qs.values())
            dataframe['client_id'] = dataframe['client_id'].apply(get_client_from_id)
            dataframe['salesman_id'] = dataframe['salesman_id'].apply(get_salesman_from_id)
            dataframe['created'] = dataframe['created'].apply(lambda x: x.strftime('%Y-%m-%d'))
            dataframe['updated'] = dataframe['updated'].apply(lambda x: x.strftime('%Y-%m-%d'))
            dataframe.rename({'client_id':'client', 'salesman_id':'salesman', 'id':'order_id'}, axis=1, inplace=True)

            positions_data = []
            for order in orders_qs:
                for pos in order.get_positions():
                    obj = {
                        'position_id': pos.id,
                        'product': pos.product.name,
                        'quantity': pos.quantity,
                        'price': pos.price,
                        'order_id': pos.get_order_id(),
                    }
                    positions_data.append(obj)

            positions_df = pd.DataFrame(positions_data)
            merged_df = pd.merge(dataframe, positions_df, on='order_id')

            dataframe = dataframe.to_html()
            positions_df = positions_df.to_html()
            merged_df = merged_df.to_html()

    context = {
        'form':form,
        'dataframe':dataframe,
        'positions_df':positions_df,
        'merged_df':merged_df,
    }
    return render(request, 'orders/search.html', context)


class OrderListView(ListView):
    model = Order
    template_name = 'orders/list.html'

class OrderDetailView(DetailView):
    model = Order
    template_name = 'orders/detail.html'