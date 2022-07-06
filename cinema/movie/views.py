import io
from django.shortcuts import render
from .models import Movie
from .torrent import make_magnet_from_file
from django.core.files import File

# Create your views here.

def all_things(request):
   movies = Movie.objects.all()
   return render(request, 'ListOfFilms.html', {'movies': movies})

def all_films(request):
   movies = Movie.objects.filter(type = 2)
   return render(request, 'ListOfFilms.html', {'movies': movies})

def all_animes(request):
   movies = Movie.objects.filter(type = 1)
   return render(request, 'ListOfFilms.html', {'movies': movies})

def all_serials(request):
   movies = Movie.objects.filter(type = 3)
   return render(request, 'ListOfFilms.html', {'movies': movies})


def player(request, film_id):
   film = Movie.objects.get(movieId=film_id)
   magnet = make_magnet_from_file(film_id)
   return render(request, 'player.html', {'film': film, 'magnet': magnet})

