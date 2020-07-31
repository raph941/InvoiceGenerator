from django.shortcuts import render
from django.contrib.auth import views as auth_views
from accounts.forms import SignupForm
from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect, render

from accounts.models import User


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