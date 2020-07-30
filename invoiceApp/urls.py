from django.conf.urls import url

from invoiceApp import views

urlpatterns = [
    url(r"$", views.home, name="home"),
]
