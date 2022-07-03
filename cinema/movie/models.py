from django.db import models

# Create your models here.


class Movie(models.Model):
    name = models.CharField(max_length=40)
    link = models.CharField(max_length=200)
    image = models.ImageField(upload_to='movie')
    rate = models.IntegerField(null=False)
    movieId = models.IntegerField(null=False)
    torrent = models.FileField(upload_to='torrent')

    class Meta:
        verbose_name = 'Фильм'
        verbose_name_plural = 'Фильм'

    def __str__(self):
        return self.name
