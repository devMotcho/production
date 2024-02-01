from django.urls import path
from .views import(
    search,
    OrderDetailView,
    OrderListView,
)
app_name = 'orders'

urlpatterns = [
    path('', search, name='search'),
    path('list/', OrderListView.as_view(), name='list'),
    path('detail/<str:pk>/', OrderDetailView.as_view(), name='detail'),

]