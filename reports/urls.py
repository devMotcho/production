from django.urls import path

from .views import (
    ReportListView,
)

app_name = 'reports'

urlpatterns = [
    path('', ReportListView.as_view(), name='list'),
]