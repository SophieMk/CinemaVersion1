from django.db import models

class UserManager(models.Manager):
    def create_user(self, login, password, email, ava):
        user = self.create(login=login, password=password, email=email, ava=ava)
        return user

class User(models.Model):
    login = models.CharField(max_length=20)
    password = models.CharField(max_length=20)
    email = models.CharField(max_length=50)
    ava = models.ImageField(upload_to='avatar', blank=True)

    objects = UserManager()

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        return self.login