import generics as generics
from django.db import models
from django.shortcuts import redirect

#class movieScore(models.Model):
#    movieId = models.IntegerField(null=False)
#    score = models.SmallIntegerField()


class UserManager(models.Manager):
    def create_user(self, login, password, email, ava):
        user = self.create(login=login, password=password, email=email, ava=ava)
        return user

    def get_password(self, log):
        user = User.objects.get(login=log)
        return user.password

    def get_email(self, log):
        user = User.objects.get(login=log)
        return user.email

    def get_ava(self, log):
        user = User.objects.get(login=log)
        print(user.ava)


class User(models.Model):
    login = models.CharField(max_length=20)
    password = models.CharField(max_length=20)
    email = models.CharField(max_length=50)
    ava = models.ImageField(upload_to='avatar', blank=True)
    #movie = models.ForeignKey(movieScore)
    objects = UserManager()

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        return self.login