from django.urls import path

from .views import (
    ReportListView,
    ReportDetailView,
    UploadTemplateView,
    csv_upload,
    createReport
)

app_name = 'reports'

urlpatterns = [
    path('list/', ReportListView.as_view(), name='list'),
    path('upload/', csv_upload, name='upload'),
    path('from-file/', UploadTemplateView.as_view(), name='from-file'),
    path('create-report/', createReport, name='create-report'),

    path('detail/<str:pk>/', ReportDetailView.as_view(), name='detail'),

]