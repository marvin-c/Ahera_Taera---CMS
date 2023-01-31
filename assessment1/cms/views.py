from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect


# from .models import

# Create your views here.
def home(request):
    return render(request, 'home.html', {})

def login_user(request):
    # return render(request, 'login.html', {})
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            # Redirect to a success page.
            return redirect('home')
        else:
            # Return an 'invalid login' error message.
            messages.success(request, ("Invalid username or password."))
            return render(request, 'login.html', {})

    else:
        return render(request, 'login.html', {})

def register_user(request):
    return render(request, 'register.html', {})