from lib2to3.fixes.fix_input import context

from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User

from django.shortcuts import render, redirect

from realEstate_app.models import Property


# Create your views here.
def index(request):
    return render(request, 'index.html')


def about(request):
    return render(request, 'about.html')


def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            messages.info(request, 'Invalid username or password.')
            return redirect('login')
    else:
        return render(request, 'registration/login.html')


def logout_user(request):
    logout(request)
    return redirect('/')


def signup(request):
    if request.method == 'POST':
        first_name = request.POST['firstname']
        last_name = request.POST['lastname']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm-password']

        if password != confirm_password:
            messages.info(request, 'Passwords must match.')
            return redirect('signup')
        if User.objects.filter(username=username).exists():
            messages.info(request, 'Username already taken.')
            return redirect('signup')
        if User.objects.filter(email=email).exists():
            messages.info(request, 'Email already taken.')
            return redirect('signup')
        else:
            user = User.objects.create_user(username, email, password, first_name=first_name, last_name=last_name)
            user.save()
            return redirect('login')
    else:
        return render(request, 'registration/signup.html')


def properties(request):
    property_list = Property.objects.all()
    return render(request, 'index.html', context={'properties': property_list})


def all_property(request):
    return render(request, 'properties.html')