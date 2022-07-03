from django.http import request
from django.shortcuts import render
from django.views.generic import TemplateView

from .forms import registrationForm, log_inForm
from .models import User, UserManager
# Create your views here.

def forms(request):
    if request.method == "POST":
        form = registrationForm(request.POST)
        if form.is_valid():
            login = form.cleaned_data.get("login")
            password = form.cleaned_data.get("password")
            email = form.cleaned_data.get("email")
            ava = form.cleaned_data.get("ava")
            User.objects.create_user(login, password, email, ava)
    else:
        form = registrationForm()
    if request.method == "POST":
        log_in = log_inForm(request.POST)
        if log_in.is_valid():
            log_in.save()
    else:
        log_in = log_inForm()
    return render(request, 'auth.html', {'form': form, 'log_in': log_in})
