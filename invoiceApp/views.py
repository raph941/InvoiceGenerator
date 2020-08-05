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

@login_required
def invoicePreviewView(request):
    return render(request, 'invoice-preview.html')

def faqView(request):
    return render(request, 'faq.html')

def contactView(request):
    return render(request, 'contact.html')
