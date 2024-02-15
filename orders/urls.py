from django.urls import path
from .views import(
    search,
    OrderDetailView,
    orderView,
    createOrder,
)
app_name = 'orders'

urlpatterns = [
    path('', search, name='search'),
    path('list/', orderView, name='list'),
    path('detail/<str:pk>/', OrderDetailView.as_view(), name='detail'),
    path('create/', createOrder, name='create'),

]