"""InvoiceGenerator URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url
from accounts import views as account_views
from invoiceApp import views as invoice_views
from . import views


urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r"about/$", views.aboutView, name="about"),
    url(r"faq/$", views.faqView, name="faq"),
    url(r"contact/$", views.contactView, name="contact"),
    url(r"pricing/$", views.pricingView, name="pricing"),
    url(r"user-statistic/$", views.userStatisticsView, name="statistics"),
    url(r"guide/$", views.invoiceGuideView, name="giude"),
    url(r"dashboard/$", views.dashboardView, name="contact"),

    url('invoice/', include('invoiceApp.urls')),
    #authentication urls
    url(r"signup/$", account_views.SignupView, name="signup"),
    url('^', include('django.contrib.auth.urls')),

    path('admin/', admin.site.urls),
]
