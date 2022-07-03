import csv
import io
import datetime
import xlwt
from django.contrib import messages
from django.db.models import Sum, ExpressionWrapper, F, DecimalField, Case, When
from django.http import HttpResponse
from django.shortcuts import render
from .models import Inventory, Product_Library, Manufacture, Price_List
from ENKI_COMPANY.models import Client_Directory, Parent_Company_Information, Child_Company_Information


#Inventory related views
def inventory_specific(request, pk):
    location = Child_Company_Information.objects.values('company_location', 'child_company_id').filter(child_company_id__exact=pk)[0]
    droplist = Child_Company_Information.objects.values('company_location', 'child_company_id')
    inventory = Inventory.objects.values('product_code__product_code', 'product_code__categorisation', 'product_code__manufacturer__manufacturer', 'product_code__product_type', 'product_code__description', 'quantity', 'inventory_location__company_location', 'inventory_location__child_company_id').filter(inventory_location__child_company_id__exact=pk).annotate(total=Sum(ExpressionWrapper(F('quantity'), output_field=DecimalField(0.00))))
    context = {'droplist':droplist, 'inventory':inventory, 'location': location}
    return render(request, 'ENKI_INVENTORY/inventory-specific.html', context)


def inventory(request):
    location = "All Locations"
    droplist = Child_Company_Information.objects.values('company_location', 'child_company_id')
    inventory = Inventory.objects.values('product_code__product_code').distinct().annotate(total=Sum(ExpressionWrapper(F('quantity'), output_field=DecimalField(0.00))), product_code__categorisation=F('product_code__categorisation'), product_code__manufacturer__manufacturer=F('product_code__manufacturer__manufacturer'), product_code__product_type=F('product_code__product_type'), product_code__description=F('product_code__description'))
    date = datetime.date.today()
    date = date.strftime("%A - %B %d, %Y")
    context = {'A':location, 'date': date, 'droplist': droplist, 'inventory':inventory, 'location':location}
    return render(request, 'ENKI_INVENTORY/inventory-alt.html', context)