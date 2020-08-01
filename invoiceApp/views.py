from django.shortcuts import render
from .models import InvoiceModel
from django.contrib.auth.decorators import login_required
from .sheet import user_invoice
from django.http import HttpResponse
from django.views.static import serve
import os


def invoiceCreationView(request):
    invoice_number = len(InvoiceModel.objects.all()) + 1
    str_in = str(invoice_number)
    inv_num = str_in.zfill(6)
    
    context = {
        'invoice_number': inv_num,
    }

    print(context)

    return render(request, 'invoice-creation.html', context)

#view for downloading the excelsheet
def excelGenerationView(request):
    if(request.POST):
        invoicedata = request.POST.dict()
        duedate = invoicedata['due_date']
        invoicedate = invoicedata['invoice_date']
        companyname = invoicedata['company_name']
        companyaddress = invoicedata['company_address']
        companycity = invoicedata['company_city']
        companycountry = invoicedata['companycountry']
        clientname = invoicedata['client_name']
        clientaddress = invoicedata['client_address']
        clientcountry = invoicedata['client_country']
        clientcity = invoicedata['client_city']
        invoiceitems = invoicedata['invoice_items']
        subtotal = invoicedata['subtotal']
        salestax = invoicedata['sales_tax']
        note = invoicedata['note']
        terms = invoicedata['terms']
        user_invoice(invoicedate,duedate,companyname,companyaddress,companycity,companycountry,clientname,clientaddress,clientcity,clientcountry,invoiceitems,subtotal,salestax,note,terms)
        filepath = './invoice.xlsx'
        return serve(request,os.path.basename(filepath),os.path.dirname(filepath))

@login_required
def invoicePreviewView(request):
    return render(request, 'invoice-preview.html')


def faqView(request):
    return render(request, 'faq.html')


def contactView(request):
    return render(request, 'contact.html')
