from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, DetailView, TemplateView
from django.http import HttpResponse, JsonResponse
import os
from django.conf import settings
from django.template.loader import get_template
from xhtml2pdf import pisa
from django.contrib.staticfiles import finders
import csv
from django.utils.dateparse import parse_date




# my app imports
from .models import Report
from orders.models import Order, Position, CSV
from product.models import Product
from human.models import Client, Profile
from .utils import get_image

class ReportListView(ListView):
    model = Report
    template_name = 'reports/list.html'

class ReportDetailView(DetailView):
    model = Report
    template_name = 'reports/detail.html'

class UploadTemplateView(TemplateView):
    template_name = 'reports/from_file.html'

def csv_upload(request):
    if request.method == 'POST':
        csv_file_name = request.FILES.get('file').name
        csv_file = request.FILES.get('file')
        obj, created = CSV.objects.get_or_create(file_name=csv_file_name)

        if created:
            obj.csv_file = csv_file
            obj.save()
            with open(obj.csv_file.path, 'r') as f:
                reader = csv.reader(f)
                reader.__next__() # skip first row
                for row in reader:
                    transaction_id = row[1]
                    product = row[2]
                    quantity = row[3]
                    client = row[4]
                    date = parse_date(row[5])
                    
                    try:
                        product_obj = Product.objects.get(name=product)
                    except Product.DoesNotExist:
                        product_obj = None

                    if product_obj is not None:
                        client_obj, _ = Client.objects.get_or_create(name=client)
                        salesman_obj = Profile.objects.get(user=request.user)

                        position_obj = Position.objects.create(
                            product=product_obj,
                            quantity=quantity,
                            created=date,
                        )
                        order_obj, _ = Order.objects.get_or_create(
                            transaction_id=transaction_id,
                            client=client_obj,
                            salesman=salesman_obj,
                            created=date,
                        )
                        order_obj.positions.add(position_obj)
                        order_obj.save()
                return JsonResponse({'ex':False})
        else:
            return JsonResponse({'ex':True})
    
    return HttpResponse()

def createReport(request):
    if request.is_ajax():
            image = request.POST.get('image')
            img = get_image(image)

            profile = request.user.profile

            Report.objects.create(
                name=request.POST.get('name'),
                text=request.POST.get('text'),
                image = img,
                author=profile,
            )
            return JsonResponse({'msg':'send'})
    return JsonResponse({})


def renderPDF(request, pk):
    template_path = 'reports/pdf.html'
    obj = get_object_or_404(Report, pk=pk)
    context = {'obj':obj}

    response = HttpResponse(content_type='application/pdf')

    response['Content-Disposition'] = 'filename="report.pdf"'

    template=get_template(template_path)
    html = template.render(context)

    #create a pdf with pisa
    pisa_status = pisa.CreatePDF(
        html, dest=response
    )
    if pisa_status.err:
        return HttpResponse('Algo deu errado <pre>' + html + '</pre>')
    return response