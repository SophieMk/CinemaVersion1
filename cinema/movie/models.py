from django.db import models

# Create your models here.
class movie(models.Model):
    name = models.CharField(max_length = 40)
    link = models.CharField(max_length = 200)
    image = models.ImageField(upload_to = 'movie')
    rate = models.IntegerField(null = False)
    id = models.IntegerField(null = False)


    class Meta:
        verbose_name = 'Фильм'
        verbose_name_plural = 'Фильм'


    def __str__(self):
        return self.name