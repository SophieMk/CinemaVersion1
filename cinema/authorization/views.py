from django.shortcuts import render
from models import User
from .forms import registrationForm
# Create your views here.

def reg_form(request):
    if request.methos == "POST":
        form = registrationForm(request.POST)
        if form.is_valid():
            form.save()
        else:
            form =registrationForm()
        return render(request, 'auth.html', {'form' : form})