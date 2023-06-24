from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

# Create your views here.


def register(request):
    if request.method == "POST":
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')

        user = User.objects.filter(username=username)

        if user.exists():
            messages.error(request, "Username Exists")
            return redirect("/register/")

        user = User.objects.create(
            first_name=first_name,
            last_name=last_name,
            username=username,
            email = email
        )

        user.set_password(password)
        user.save()
        return redirect('/login/')
    return render(request, 'register.html')


def login_page(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)
        if not User.objects.filter(username=username).exists():
            messages.warning(request, 'Invalid username', extra_tags=username)
            print('working')
            return render(request, 'login.html')
        elif user is None:
            messages.error(request, 'Password is incorrect')
            print(messages)

        else:
            login(request, user)
            return redirect('/')

    return render(request, 'login.html')


@login_required(login_url='/login/')
def home(request):
    return render(request, 'home.html')


def logout_page(request):
    logout(request)
    return redirect('/login/')
