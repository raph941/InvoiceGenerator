from django.shortcuts import render
from .models import InvoiceModel
from django.contrib.auth.decorators import login_required
from .sheet import user_invoice
from django.http import HttpResponse


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
    if(request.post):
        invoicedata = request.POST.dict()
        duedate = invoicedata.duedate
        invoicedate = invoicedata.invoice_date
        companyname = invoicedata.company_name
        companyaddress = invoicedata.companyaddress
        companycity = invoicedata.companycity
        companycountry = invoicedata.companycountry
        clientname = invoicedata.client_name
        clientaddress = invoicedata.client_address
        clientcountry = invoicedata.client_country
        clientcity = invoicedata.client_city
        invoiceitems = invoicedata.invoiceitems
        subtotal = invoicedata.subtotal
        salestax = invoicedata.sales_tax
        note = invoicedata.note
        terms = invoicedata.terms
        user_invoice(invoicedate,duedate,companyname,companyaddress,companycity,companycountry,clientname,clientaddress,clientcity,clientcountry,invoiceitems,subtotal,salestax,note,terms)
        file = "/static/invoice.xlsx"
        response = HttpResponse(file,content_type='application/ms-excel')
        response['Content-Disposition'] = 'attachment; filename="invoice.xlsx"'
        return response

@login_required
def invoicePreviewView(request):
    return render(request, 'invoice-preview.html')


def faqView(request):
    return render(request, 'faq.html')


def contactView(request):
    return render(request, 'contact.html')
