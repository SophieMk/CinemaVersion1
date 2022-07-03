from django.shortcuts import render, redirect
from .forms import registrationForm, log_inForm
from .models import User, UserManager

def reg_form(request):
    if request.method == "POST":
        form = registrationForm(request.POST)
        if form.is_valid():
            login = form.cleaned_data.get("login")
            password = form.cleaned_data.get("password")
            email = form.cleaned_data.get("email")
            ava = form.cleaned_data.get("ava")
            User.objects.create_user(login, password, email, ava)
            return redirect('http://127.0.0.1:8000/')
    else:
        form = registrationForm()
    return render(request, 'auth.html', {'form': form})

def log_in_form(request):
    if request.method == "POST":
        log_in = log_inForm(request.POST)
        if log_in.is_valid():
            log_in.save()
            return redirect('http://127.0.0.1:8000/')
    else:
        log_in = log_inForm()
    return render(request, 'log_in.html', {'log_in': log_in})
