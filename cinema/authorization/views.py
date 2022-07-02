from django.shortcuts import render
from .forms import registrationForm
from .models import User, UserManager
# Create your views here.

def reg_form(request):
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
    return render(request, 'auth.html', {'form':form})


