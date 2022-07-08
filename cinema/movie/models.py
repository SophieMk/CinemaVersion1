from django.db import models

# Create your models here.


class nScore(models.Model):
    amount = models.IntegerField()
    inter_score = models.SmallIntegerField()

class Movie(models.Model):

    TYPES = {
        (1, 'Аниме'),
        (2, 'Фильм'),
        (3, 'Сериал')
    }

    name = models.CharField(max_length=40)
    type = models.PositiveSmallIntegerField( ("type"), choices=TYPES, null=True)
    description = models.CharField(max_length=300, null=True)
    link = models.CharField(max_length=200)
    image = models.ImageField(upload_to='movie')
    rate = models.IntegerField(null=False)
    movieId = models.IntegerField(null=False)
    torrent = models.FileField(upload_to='torrent', null=True)
    movieTotalScore = models.ForeignKey(nScore, on_delete=models.CASCADE, null=True)


    class Meta:
        verbose_name = 'Фильм'
        verbose_name_plural = 'Фильм'

    def __str__(self):
        return self.name
