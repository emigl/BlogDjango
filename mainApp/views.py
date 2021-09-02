from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
# Custom Form
from mainApp.forms import RegisterForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout

# Views

def index(request):

    return render(request, 'mainApp/index.html', {
        'title': 'Home',
        'title2': 'Django\'s blog'
    })

def about(request):

    return render(request, 'mainApp/about.html', {
        'title': 'About us'
    })


def register_page(request):

    if request.user.is_authenticated:
        return redirect('index')

    else:
        register_form = RegisterForm()

        if request.method == 'POST':
            register_form = RegisterForm(request.POST)

            if register_form.is_valid():
                register_form.save()
                messages.success(request, 'You can login now with your user and password!')
                return redirect('login')

        return render(request, 'users/register.html', {
            'title': 'Sign up',
            'register_form': register_form
        })


def login_page(request):

    if request.user.is_authenticated:
        return redirect('index')

    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')
            
            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                messages.success(request, f'You are login as {username}!')
                return redirect('index')
                
            else:
                messages.warning(request, 'The credentials do not match!')



        return render(request, 'users/login.html', {
            'title': 'Sign in'
        })

def logout_user(request):
    logout(request)

    return redirect('login')