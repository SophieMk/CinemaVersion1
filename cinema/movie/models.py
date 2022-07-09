from django.db import models

class MovieManager(models.Manager):
    def get_name(self, movie_id):
        movie = Movie.objects.get(movieId=movie_id)
        return movie.name

class Movie(models.Model):

    objects = MovieManager()
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
    NUsersEstimated = models.IntegerField(null=True)
    inter_score = models.FloatField(null=True)
    movieTotalScore = models.FloatField(null=True)

    class Meta:
        verbose_name = 'Фильм'
        verbose_name_plural = 'Фильм'

    def __str__(self):
        return self.name
