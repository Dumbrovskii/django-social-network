from django.shortcuts import render, redirect
from core.forms import UserRegisterForm
from django.contrib import messages


def home(request):
    if request.user.is_authenticated:
        return render(request, "feed/index.html")

    return render(request, "landing.html")

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.clean_username()
            messages.success(request, f'Your account has been created! You are now able to log in {username}')
            return redirect('login')
    else:
        form = UserRegisterForm()

    return render(request, 'registration/register.html', {'form': form})