from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from log.forms import RegisterForm

@login_required(login_url='login')
def home(request):
    return render(request, "home.html")

def register(request):
    if request.method == "POST":
        username = request.POST.get('username', None)
        email = request.POST.get('email', None)
        password = request.POST.get('password', None)
        password_again = request.POST.get('password_again', None)
        if password != password_again:
            register = RegisterForm()
            return render(request, 'register.html', {
                'register_form': register,
                'error_message': "Passwords not match",
            })
        user, created = User.objects.get_or_create(username=username, email=email)
        if created:
            user.set_password(password)
            user.save()
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect("/")
        return redirect("/login")

    else:
        register = RegisterForm()
        return render(request, "register.html", {'register_form': register})
