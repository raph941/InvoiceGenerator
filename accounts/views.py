from django.shortcuts import render
from django.contrib.auth import views as auth_views
from accounts.forms import SignupForm
from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth import authenticate, login
from django.http import HttpResponse, HttpResponseRedirect
import json

from accounts.models import User


def AjaxloginView(request):
    email= request.POST.get('email')
    password = request.POST.get('password')
    user = authenticate(email=email, password=password)
    if user is not None:
        if user.is_active:
            login(request, user)
            return HttpResponse(json.dumps({"message": "Success"}),content_type="application/json")
        else:
            return HttpResponse(json.dumps({"message": "inactive"}), content_type="application/json")
    else:
        return HttpResponse(json.dumps({"message": "invalid"}),content_type="application/json")
    return HttpResponse(json.dumps({"message": "denied"}),content_type="application/json")


# Create your views here.
def SignupView(request):
    form = SignupForm(request.POST)
    if request.method == 'POST':
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()
            user.is_regular = True
            user.save()
        
            return redirect('login')
        else:
            form = SignupForm()
            
            #to vary the message to be shown to the user based on the nature of validationerror they make
            mail = request.POST['email']
            password1 = request.POST['password1']
            password2 = request.POST['password2']

            if User.objects.filter(email=mail).exists():
                messages.error(request, "A user with thesame Email already exists")
            if password1 and password1 != password2:
                messages.error(request, "passwords did not match")

    return render(request, 'registration/signup.html', {'form': form})