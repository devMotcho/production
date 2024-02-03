from django.shortcuts import render
from django.views.generic import ListView, DetailView


# my app imports
from .models import Report

class ReportListView(ListView):
    model = Report
    template_name = 'reports/list.html'
