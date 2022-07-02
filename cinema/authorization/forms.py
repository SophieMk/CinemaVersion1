from django import forms
from .models import User

class registrationForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ["login", "password1", "password2", "email", "avatar"]
        labels = {'login' : "Логин", 'password1' : "Пароль", 'password2' : "Повторите пароль",
                  'email' : "Электронная почта", 'avatar' : "Аватар"}

