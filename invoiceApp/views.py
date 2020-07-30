from django.shortcuts import render


def home(request):
    return render(request, 'base.html')


def invoiceCreationView(request):
    return render(request, 'invoice-creation.html')


def faqView(request):
    return render(request, 'faq.html')
