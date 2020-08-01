from django.conf.urls import url

from invoiceApp import views

urlpatterns = [
    url(r"create/$", views.invoiceCreationView, name="create_invoice"),
    url(r"preview/$", views.invoicePreviewView, name="invoice_preview"),
    url(r"excel/$", views.excelGenerationView,  name="generate_excel"),
]
