from django.db import models
from accounts.models import User


class InvoiceModel(models.Model):
    freelancer          = models.ForeignKey(User, verbose_name=("freelancer"), on_delete=models.CASCADE)
    company_name        = models.CharField(max_length=550, null=True, blank=True)
    company_address     = models.CharField(max_length=550, null=True, blank=True)
    company_city        = models.CharField(max_length=550, null=True, blank=True)
    company_country     = models.CharField(max_length=550, null=True, blank=True)
    client_name         = models.CharField(max_length=550, null=True, blank=True)
    client_address      = models.CharField(max_length=550, null=True, blank=True)
    client_city         = models.CharField(max_length=550, null=True, blank=True)
    client_country      = models.CharField(max_length=550, null=True, blank=True)
    invoice_number      = models.IntegerField(blank=True, default=0, verbose_name=('invoice_number'))

    def __str__(self):
        return f'Invoice Number : { self.invoice_number }'