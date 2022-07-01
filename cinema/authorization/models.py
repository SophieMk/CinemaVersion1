from django.db import models

class User(models.Model):
    login = models.CharField(max_length=20)
    password = models.CharField(max_length=20)
    user_name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    ava = models.ImageField(upload_to='avatar')
    id_user = models.IntegerField(null=False)

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'