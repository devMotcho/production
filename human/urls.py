from django.urls import path

from .views import(
    employeesList,
    employeeCreate,
    employeeUpdate,
    employeeDelete,
    employeeView,

    loginPage,
    logoutUser
)

app_name='human'

urlpatterns = [
    path('login/', loginPage, name='login'),
    path('logout/', logoutUser, name='logout'),


    path('', employeesList, name='list'),
    path('create/', employeeCreate, name='create'),
    path('update/<str:pk>/', employeeUpdate, name='update'),
    path('delete/<str:pk>/', employeeDelete, name='delete'),
    path('<str:pk>/', employeeView, name='view'),



]