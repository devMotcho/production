from django.urls import path

from .views import (
    productList,
    productCreate,
    productUpdate,
    productDelete,
    productView,

    inventaryView,

    productionView,
    addProduction,
    productionEdit,
    productionDelete,

    productionOrderView,
)

app_name = 'product'


urlpatterns = [
    #Product
    path('', productList, name='list'),
    path('create/', productCreate, name='create'),
    path('update/<str:pk>/', productUpdate, name='update'),
    path('delete/<str:pk>/', productDelete, name='delete'),
    path('product/<str:pk>/', productView, name='view'),

    #Inventary
    path('inventary/', inventaryView, name="inv"),

    #Productions
    path('production/', productionView, name='prod'),
    path('add-prod/', addProduction, name='add-prod'),
    path('prod-edit/<str:pk>/', productionEdit, name='prod-edit'),
    path('prod-del/<str:pk>/', productionDelete, name='prod-del'),

    #Ordem Produção
    path('productionOrderView/', productionOrderView, name='production-order'),
]
