from django.shortcuts import render
from .models import Movie
from .torrent import get_magnet

# Create your views here.


def all_films(request):
   movies = Movie.objects.all()
   return render(request, 'ListOfFilms.html', {'movies': movies})


def player(request, film_id):
   film = Movie.objects.get(movieId=film_id)
   magnet = get_magnet(film_id)
   return render(request, 'player.html', {'film': film, 'magnet': magnet})

