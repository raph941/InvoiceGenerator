from django.shortcuts import render
from django.contrib.auth import views as auth_views
from accounts.forms import SignupForm
from django.shortcuts import get_object_or_404, redirect, render


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
    return render(request, 'registration/signup.html', {'form': form})