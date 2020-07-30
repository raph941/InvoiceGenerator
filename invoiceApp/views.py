from django.shortcuts import render
from .models import InvoiceModel
from django.contrib.auth.decorators import login_required


def home(request):
    return render(request, 'base.html')

def invoiceCreationView(request):
    invoice_number = len(InvoiceModel.objects.all()) + 1

    context = {
        'invoice_number': invoice_number,
    }
    print(context)

    return render(request, 'invoice-creation.html', context)

@login_required
def invoicePreviewView(request):
    return render(request, 'invoice-preview.html')


def faqView(request):
    return render(request, 'faq.html')
