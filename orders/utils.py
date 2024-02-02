import uuid, base64
from io import BytesIO
import matplotlib.pyplot as plt
import seaborn as sns

#my apps imports
from human.models import Client, Profile


def generate_code():
    code = str(uuid.uuid4()).replace('-', '').upper()[:12]
    return code

def get_client_from_id(val):
    client = Client.objects.get(id=val)
    return client

def get_salesman_from_id(val):
    salesman = Profile.objects.get(id=val)
    return salesman

def get_graph():
    buffer = BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    image_png = buffer.getvalue()
    graph = base64.b64encode(image_png)
    graph = graph.decode('utf-8')
    buffer.close()
    return graph

def get_key(res_by):
    if res_by == '#1':
        key = 'transaction_id'
    if res_by == '#2':
        key = 'created'
    return key

def get_chart(chart_type, data, results_by, **kwargs):
    plt.switch_backend('AGG')
    fig = plt.figure(figsize=(10,4))
    key = get_key(results_by)
    d = data.groupby(key, as_index=False)['total_price'].agg('sum')

    #bar
    if chart_type == '#1':
        sns.barplot(x=key, y='total_price', data=d)
    else:
        pass

    chart = get_graph()
    return chart