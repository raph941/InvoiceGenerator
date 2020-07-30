from django.conf.urls import url

from accounts import views

urlpatterns = [
    url(r"^SignUp/$", views.SignupView, name="signup"),
]
